from django.urls import path
from accounts.views import CreateUserView
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('register', CreateUserView.as_view(), name='register'),
    path('token', obtain_auth_token, name='token'),
]
