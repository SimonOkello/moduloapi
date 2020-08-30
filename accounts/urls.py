from django.urls import path

from .views import Register, LoginApiView, VerifyEmail


urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('verify_email/', VerifyEmail.as_view(), name='verify-email'),

]
