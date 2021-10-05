from rest_framework import permissions
from rest_framework.generics import CreateAPIView, views
from django.contrib.auth import get_user_model # If used custom user model
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from rest_framework.response import Response


class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]


class CurrentUserView(views.APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        user = get_user_model().objects.get(phone=request.user.phone)
        
        return Response({
            "phone": user.phone,
            "fullname": user.fullname
        })