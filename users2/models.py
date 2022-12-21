from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user2(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user2 = self.model(email=email, **extra_fields)
        user2.set_password(password)
        user2.save()

        return User2

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("El superusuario necesita que is_staff sea verdadero")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("El superusuario necesita que is_superuser sea verdadero")
        return self.create_user(email=email, password=password, **extra_fields)


class User2(AbstractUser):
    email = models.CharField(max_length=80, unique=True, default="no@email.com")
    username = models.CharField(max_length=45)
    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def str(self):
        return self.email

    class Meta:
        db_table = "users2"