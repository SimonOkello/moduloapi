from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import Register, LoginApiView, VerifyEmail, PasswordResetAPIView, PasswordResetTokenValidation, SetNewPassword


urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('verify_email/', VerifyEmail.as_view(), name='verify-email'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('reset_password/', PasswordResetAPIView.as_view(), name='reset-password'),
    path('password_reset/<uidb64>/<token>/',
         PasswordResetTokenValidation.as_view(), name='password-reset-confirm'),
    path('password_reset_complete/', SetNewPassword.as_view(),
         name='password-reset-complete')

]
