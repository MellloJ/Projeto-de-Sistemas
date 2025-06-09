from django.core.mail import send_mail
from django.conf import settings

from rest_framework_simplejwt.tokens import RefreshToken
from datetime import timedelta
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.urls import reverse

def generateToken(user):
    refresh = RefreshToken.for_user(user)
    refresh.set_exp(lifetime=timedelta(hours=1))
    refresh['purpose']= 'email_confirmation'

    return str(refresh.access_token)


def sendMail(request, user):
    subject = 'Confirmação de Cadastro'
    token = generateToken(user.user)
    confirmationLink = request.build_absolute_uri(f'/confirm/?token={token}')
    completeName = " ".join([user.first_name, user.last_name])
    email = user.user.email
    
    context = {
        'completeName': completeName,
        'email': email,
        'link_confirmacao': confirmationLink,
    }

    htmlMessage = render_to_string('signup/confirming.html', context)

    send_mail(
        subject,
        strip_tags(htmlMessage),
        settings.DEFAULT_FROM_EMAIL,
        [email],
        html_message=htmlMessage
    )
