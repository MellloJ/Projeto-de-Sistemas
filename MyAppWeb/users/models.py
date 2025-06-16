from django.db import models
from django.conf import settings

from auth_app.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class ClientUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='client_user'
    )

    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    cpf = models.CharField(max_length=11, null=False, unique=True)
    # is_client = models.BooleanField(default=True)

    class Meta:
        db_table = 'ClientUser'

    def __str__(self):
        return f"Cliente: {self.user.email}"

class DeliveryUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='delivery_user'
    )

    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    cpf = models.CharField(max_length=11, null=False, unique=True)

    class Meta:
        db_table = 'DeliveryUser'

    def __str__(self):
        return f"Entregador: {self.user.email}"
    
class SupermarketUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='supermarket_user'
    )

    fantasy_name = models.CharField(max_length=255, null=False)
    cnpj = models.CharField(max_length=18, null=False, unique=True)

    class Meta:
        db_table = 'SupermarketUser'

    def __str__(self):
        return f"Supermercado: {self.name}"

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=20, null=True, blank=True)
    street = models.CharField(max_length=255, null=False)
    number = models.CharField(max_length=20, null=True, blank=True)
    complement = models.CharField(max_length=100, null=True, blank=True)
    neighborhood = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=2, null=False)

    class Meta:
        db_table = 'Address'
    
    def __str__(self):
        return f"{self.street}, {self.number}"
    
class SeparaterUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='separater_user'
    )

    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    cpf = models.CharField(max_length=11, null=False, unique=True)

    class Meta:
        db_table = 'SeparaterUser'

    def __str__(self):
        return f"Separador: {self.user.email}"