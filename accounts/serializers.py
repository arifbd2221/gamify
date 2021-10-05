from rest_framework import serializers
from django.contrib.auth import get_user_model # If used custom user model

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        
        user = UserModel(
            phone=f"019{validated_data['phone']}",
            fullname=validated_data['fullname'],
        )
        user.set_password(f"019{validated_data['phone']}")
        user.save()

        return user

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ( "id", "fullname", "phone", )