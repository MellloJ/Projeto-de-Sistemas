from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.timezone import now
from auth_app.models import User, UserManager

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
            return user
        except Exception as e:
            raise ValidationError(f"Erro ao criar usuário: {str(e)}")