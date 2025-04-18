from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O email é obrigatório')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):

    email = models.CharField(max_length=30, null=False, unique=True)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=120, null=False)
    completeName = models.CharField(max_length=150, null=False, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    password = models.CharField(null=False)

    #username = models.CharField(max_length=150, null=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=False)
    date_joined = models.DateTimeField(null=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['completeName', 'password']

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email

class Address():
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.TextField()
    state = models.TextField()
    street = models.TextField()
    number = models.CharField(max_length=20)
    neighborhood = models.CharField(max_length=50)

    class Meta:
        db_table = 'addresses'
    
    def __str__(self):
        return self.street