from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.validators import validate_email
from django.db import transaction, IntegrityError
from auth_app.models import User, UserManager
from users.models import ClientUser

class signupClient:
    def checkUserExist(email):
        try:
            user = User.objects.get(email=email)
            return True
        except User.DoesNotExist:
            return False
    
    def register(email, password, cpf, first_name, last_name, user_type, phone=None):
        #completeName = " ".join([first_name, last_name])
        
        #group = Group.add('user')
        #permission = Permission.add('user')

        try:
            with transaction.atomic():
                user = User.objects.create_user(
                    email=email,
                    password=password,
                    user_type=user_type,
                    phone=phone
                )
                if user is not None:
                    clientUser = ClientUser.objects.create(
                        user=user,
                        first_name=first_name,
                        last_name=last_name,
                        cpf=cpf,
                    )
                else:
                    raise ValidationError("Erro ao criar usuário, tente novamente.")
            return clientUser, "Usuário criado com sucesso, confirme seu email"
        except IntegrityError as e:
            return None, "E-mail ou CPF já está em uso."

        except ValidationError as e:
            return None, e.messages

        except Exception as e:
            return None, f"Erro inesperado: {str(e)}"
