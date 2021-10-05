from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        """
        Creates and saves a User with the given phone and password.
        """
        if not phone:
            raise ValueError('Users must have a phone number')

        user = self.model(
            phone=phone,
        )

        user.set_password(password)
        user.staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    phone = models.CharField(max_length=11, unique=True, null=False, blank=False)
    fullname = models.CharField(max_length=64, default="N/A")
    USERNAME_FIELD = 'phone'
    
    objects = UserManager()
