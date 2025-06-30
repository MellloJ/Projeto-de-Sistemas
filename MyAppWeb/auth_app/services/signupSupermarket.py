from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.validators import validate_email
from django.utils.timezone import now
from django.db import transaction, IntegrityError
from auth_app.models import User

class signupSupermarket:
    @staticmethod
    def register(email, password, fantasy_name, cnpj):
        try:
            with transaction.atomic():
                user = User.objects.create_user(
                    email=email,
                    password=password,
                    user_type='supermarket'
                )
            return user, "Usuário criado com sucesso, confirme seu email"
        except IntegrityError as e:
            return None, "E-mail ou CNPJ já está em uso."
        except ValidationError as e:
            return None, e.messages
        except Exception as e:
            return None, f"Erro inesperado: {str(e)}"
