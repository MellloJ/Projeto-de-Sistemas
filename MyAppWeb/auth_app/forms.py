from django import forms
import re
from auth_app.services.validateUser import validate_cpf
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from users.models import ClientUser

class signupUserForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'autofocus': True,
        })
        )
    last_name = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'autofocus': True,
        })
        )
    cpf = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'placeholder': '000.000.000-00',
            'id': 'cpf',
        })
        )
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'placeholder': '(63)9999-9999',
            'id' : 'phone',
        })
        )
    email = forms.EmailField(
        max_length=255,
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'placeholder': 'email@dominio.com',
        })
    )
    
    class Meta:
        model = ClientUser
        fields = ['first_name', 'last_name', 'email', 'cpf', 'phone']

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf', '')

        if not cpf:
            return cpf
        else:
            cpf = validate_cpf(self, cpf)
        return cpf
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        digits = re.sub(r'\D', '', phone)

        if len(digits) != 11:
            raise ValidationError("O telefone deve conter 11 dígitos (DDD + número).")

        return digits
        

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise ValidationError("Formato de e-mail inválido.")
        return email
