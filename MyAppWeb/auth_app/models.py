from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import Group, Permission

from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password, groupName, **extra_fields):
        if not email:
            raise ValueError('O email é obrigatório')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        group, created = Group.objects.get_or_create(name=groupName)
        user.set_password(password)
        user.save(using=self._db)
        user.groups.add(group)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, null=False, unique=True)
    password = models.CharField(max_length= 128, null=False)
    phone = models.CharField(max_length=11, null=True, blank=True)
    user_type = models.CharField(max_length=20, null=False, default='client')
    photo = models.CharField(null=True, blank=True)

    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=False)
    date_joined = models.DateTimeField(null=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_type', 'password']

    class Meta:
        db_table = 'User'

    def __str__(self):
        return self.email
    