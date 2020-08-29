from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings
import jwt


# Create your views here.
from .serializers import RegisterSerializer
from .models import User
from .utils import Util


class Register(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])

        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relativeLink = reverse('verify-email')
        absolute_url = 'http://' + current_site + \
            relativeLink+"?token="+str(token)
        email_body = 'Hi '+user.username + \
            ' Please use the link below to confirm your email \n' + absolute_url
        data = {'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Confirm your Email'}

        Util.send_email(data)

        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail(GenericAPIView):
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified=True
                user.save()
            return Response({'email': 'Your account is now activated'}, status=status.HTTP_200_OK)

        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Your Activation link is expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exeptions.DecodeError as identifier:
            return Response({'error': 'Invalid token!. Please request for a new one'}, status=status.HTTP_400_BAD_REQUEST)
