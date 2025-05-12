from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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