from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

NULLABLE = {"null": True, "blank": True}


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="электронная почта")
    phone = models.CharField(max_length=50, verbose_name="телефон", **NULLABLE)
    avatar = models.ImageField(upload_to="users/", verbose_name="аватар", **NULLABLE)
    country = models.CharField(max_length=20, verbose_name="страна", **NULLABLE)
    first_name = models.CharField(max_length=25, verbose_name="имя")
    last_name = models.CharField(max_length=25, verbose_name="фамилия", **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name="активный")

    # переопределение поля user как основного для идентификации на емаил
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
