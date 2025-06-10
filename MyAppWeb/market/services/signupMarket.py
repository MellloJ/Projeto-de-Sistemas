from users.models import SupermarketUser
from auth_app.models import User
from django.utils.timezone import now
from django.db import transaction, IntegrityError
from django.core.exceptions import ValidationError

class signupMarket:
    def checkUserExist(cnpj):
        try:
            market = SupermarketUser.objects.get(cnpj=cnpj)
            return True
        except SupermarketUser.DoesNotExist:
            return False
    
    def register(name, cnpj, phone, email, password):
        try:
            with transaction.atomic():
                user = User.objects.create_user(
                    email=email,
                    password=password,
                    groupName='supermarket',
                    phone=phone,
                    last_login=now(),
                    date_joined=now()
                )
                market = SupermarketUser.objects.create(
                    user=user,
                    fantasy_name=name,
                    cnpj=cnpj
                )
            return market, "Usuário criado com sucesso, confirme seu email"
        except IntegrityError as e:
            return None, "E-mail ou CNPJ já está em uso."

        except ValidationError as e:
            return None, e.messages

        except Exception as e:
            print("Erro inesperado:", str(e))
            return None, f"Erro inesperado: {str(e)}"