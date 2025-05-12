from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.validators import validate_email
from django.utils.timezone import now
from django.db import transaction, IntegrityError
from auth_app.models import User, UserManager, Supermarket, SupermarketManager

class signupClient:
    def checkUserExist(email):
        try:
            user = User.objects.get(email=email)
            return True
        except User.DoesNotExist:
            return False
    
    def register(email, password, cpf, first_name, last_name, phone=None):
        completeName = " ".join([first_name, last_name])
        
        date_joined = now()
        last_login = now()
        #group = Group.add('user')
        #permission = Permission.add('user')

        try:
            with transaction.atomic():
                user = User.objects.create_user(
                    email=email,
                    password=password,
                    groupName='client',
                    first_name=first_name,
                    last_name=last_name,
                    completeName=completeName,
                    cpf=cpf,
                    phone=phone,
                    date_joined=date_joined,
                    last_login=last_login
                )
            return user, "Usuário criado com sucesso, confirme seu email"
        except IntegrityError as e:
            return None, "E-mail ou CPF já está em uso."

        except ValidationError as e:
            return None, e.messages

        except Exception as e:
            return None, f"Erro inesperado: {str(e)}"

class signupMarket:
    def checkUserExist(cnpj):
        try:
            user = User.objects.get(cnpj=cnpj)
            return True
        except User.DoesNotExist:
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