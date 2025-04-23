from django import forms
import re
from django.core.exceptions import ValidationError
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from .models import *

def calcDigito(digs):
    s = sum(int(digs[i]) * ((len(digs) + 1) - i) for i in range(len(digs)))
    res = 11 - s % 11
    return '0' if res >= 10 else str(res)

class signupUserForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'shadow-xs bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-xs-light',
            'autofocus': True,
        })
        )
    last_name = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'shadow-xs bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-xs-light',
            'autofocus': True,
        })
        )
    cpf = forms.CharField(
        max_length=11,
        widget=forms.TextInput(attrs={
            'class': 'shadow-xs bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-xs-light',
            'placeholder': '000.000.000-00',
        })
        )
    phone = forms.CharField(
        max_length=11,
        widget=forms.TextInput(attrs={
            'class': 'shadow-xs bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-xs-light',
            'placeholder': '(63)9999-9999',
        })
        )
    email = forms.EmailField(
        max_length=255,
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'shadow-xs bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-xs-light',
            'placeholder': 'email@dominio.com',
        })
    )
    #type="email" id="email" name="email"  
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'cpf', 'phone']

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf', '')

        if not cpf:
            return cpf

        cpf = re.sub(r'[^0-9]', '', cpf)

        if len(cpf) != 11 or cpf == cpf[0] * 11:
            raise ValidationError("CPF inválido.")

        # Validação dos dígitos verificadores

        d1 = calcDigito(cpf[:9])
        d2 = calcDigito(cpf[:9] + d1)

        if cpf[-2:] != d1 + d2:
            raise ValidationError("CPF inválido.")

        return cpf

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise ValidationError("Formato de e-mail inválido.")
        return email