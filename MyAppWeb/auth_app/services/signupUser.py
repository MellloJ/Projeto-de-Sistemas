from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.models import Group, Permission
from django.utils.timezone import now
from auth_app.models import User

class signupUser:
    def checkUserExist(email):
        try:
            user = User.objects.get(email=email)
            return True
        except User.DoesNotExist:
            return False
    
    def register(request, email, password, cpf, phone, first_name, last_name):
        completeName = (first_name, last_name)
        completeName = " ".join(completeName)

        is_superuser = False
        is_active = False
        is_staff = False
        date_joined = now()
        last_login = now()
        #group = Group.add('user')
        #permission = Permission.add('user')

        user = User(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            completeName=completeName,
            cpf=cpf,
            phone=phone,
            is_superuser=is_superuser,
            is_active=is_active,
            is_staff=is_staff,
            date_joined=date_joined,
            last_login=last_login
        )

        user.set_password(password)
        user.save()

        return user
