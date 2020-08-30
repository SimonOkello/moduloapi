from rest_framework import serializers
from django.contrib.auth import authenticate, login
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_bytes, smart_str, force_bytes,force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework.response import Response
from rest_framework import status


from .models import User
from .utils import Util


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate(self, attrs):
        username = attrs.get('username', '')
        email = attrs.get('email', '')

        if not username.isalnum():
            raise serializers.ValidationError(
                'Username should only contain alphanumeric')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(
        max_length=68, min_length=6, read_only=True)
    tokens = serializers.CharField(max_length=68, min_length=6, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials. Try again')
        if not user.is_active:
            raise AuthenticationFailed(
                'Account is inactive. Please contact admin.')
        if not user.is_verified:
            raise AuthenticationFailed('Please verify your email first.')

        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens()
        }
        return super().validate(attrs)


class PasswordResetSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(min_length=3)

    class Meta:
        model = User
        fields = ['email']


class SetNewPasswordSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        min_length=6, max_length=68, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        model = User
        fields = ['password', 'uidb64', 'token']

    def validate(self, attrs):

        try:
            password = attrs.get('password', '')
            uidb64 = attrs.get('uidb64', '')
            token = attrs.get('token', '')

            user_id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=user_id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The password reset link is invalid', status=status.HTTP_401_UNAUTHORIZED)
            user.set_password(password)
            user.save()
            return user

        except Exception as e:
            raise AuthenticationFailed('The password reset link is invalid', status=status.HTTP_401_UNAUTHORIZED)

        return super().validate(attrs)
