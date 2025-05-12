from market.models import Supermarket, SupermarketManager
from django.db import transaction, IntegrityError
from django.core.exceptions import ValidationError

class signupMarket:
    def checkUserExist(cnpj):
        try:
            market = Supermarket.objects.get(cnpj=cnpj)
            return True
        except market.DoesNotExist:
            return False
    
    def register(name, cnpj, phone, email, password):
        try:
            with transaction.atomic():
                market = Supermarket.objects.create_market(
                    cnpj=cnpj,
                    password=password,
                    email=email,
                    name=name,
                    phone=phone,
                )
            return market, "Usuário criado com sucesso, confirme seu email"
        except IntegrityError as e:
            return None, "E-mail ou CNPJ já está em uso."

        except ValidationError as e:
            return None, e.messages

        except Exception as e:
            print("Erro inesperado:", str(e))
            return None, f"Erro inesperado: {str(e)}"