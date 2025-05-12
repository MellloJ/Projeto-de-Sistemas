from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.conf import settings

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
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=120, null=False)
    completeName = models.CharField(max_length=150, null=False, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    password = models.CharField(max_length= 128, null=False)

    #username = models.CharField(max_length=150, null=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
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

class DeliverUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='deliver_user_profile'
    )

    comprovante_residencia = models.FileField(null=False)
    rg_photo = models.FileField(null=False)
    photo = models.FileField(null=False)
    cpf = models.CharField(max_length=11, null=False, unique=True)
    is_deliver = models.BooleanField(default=True)

    class Meta:
        db_table = 'deliver_users'

    def __str__(self):
        return f"Entregador: {self.user.email}"

class SupermarketManager(models.Manager):
    def create_market(self, cnpj, password, **extra_fields):
        if not cnpj:
            raise ValueError('O CNPJ é obrigatório')

        market = self.model(cnpj=cnpj, **extra_fields)
        market.set_password(password)
        market.save(using=self._db)
        return market

class Supermarket(AbstractBaseUser):
    name = models.CharField(max_length=255, null=False)
    cnpj = models.CharField(max_length=18, null=False, unique=True)
    phone = models.CharField(max_length=11, null=False)
    email = models.EmailField(max_length=255, null=False, unique=True)
    password = models.CharField(max_length=128, null=False)
    is_active = models.BooleanField(default=False)

    objects = SupermarketManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['name']

    class Meta:
        db_table = 'supermarkets'

    def __str__(self):
        return self.name

class Address():    
    city = models.TextField()
    state = models.TextField()
    street = models.TextField()
    number = models.CharField(max_length=20)
    neighborhood = models.TextField()

    # Relacionamento genérico
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    related_object = GenericForeignKey('content_type', 'object_id')
    
    class Meta:
        db_table = 'addresses'
    
    def __str__(self):
        return f"{self.street}, {self.number}"