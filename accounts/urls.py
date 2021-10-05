from django.urls import path
from accounts.views import CreateUserView, CurrentUserView
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('register', CreateUserView.as_view(), name='register'),
    path('token', obtain_auth_token, name='token'),
    path('user', CurrentUserView.as_view(), name='user'),
]
