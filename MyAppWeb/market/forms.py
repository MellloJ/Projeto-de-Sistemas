from django import forms
from .models import Supermarket

class createMarketForm(forms.ModelForm):
    name = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'autofocus': True,
        })
        )
    cnpj = forms.CharField(
        max_length=14,
        widget=forms.TextInput(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'placeholder': '00.000.000/0001-00',
        })
        )
    phone = forms.CharField(
        max_length=11,
        widget=forms.TextInput(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'placeholder': '(63)9999-9999',
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
        model = Supermarket
        fields = ['name', 'cnpj', 'phone', 'email']