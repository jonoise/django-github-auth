from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

from django.db import models
from rest_framework.fields import CharField
from rest_framework_simplejwt.tokens import RefreshToken


class MainUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise TypeError('Email is required.')
        if not password:
            raise TypeError('Password is required.')
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        super_user = self.create_user(email=email, password=password)
        super_user.is_staff = True
        super_user.is_admin = True
        super_user.save(using=self._db)
        return super_user


class MainUser(AbstractBaseUser):
    AUTH_PROVIDERS = {'local': 'local', 'github': 'github'}

    email = models.EmailField(max_length=255, unique=True, db_index=True)
    # is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    github_access_token = models.CharField(max_length=255, null=True)
    provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('local'))

    USERNAME_FIELD = 'email'

    objects = MainUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
