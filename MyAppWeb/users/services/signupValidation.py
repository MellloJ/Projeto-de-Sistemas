from django import forms

class signupForm(forms.Form):
    email = forms.EmailField()
    password =
    cpf = forms.IntegerField()
    name = forms.CharField(max_lenght="50")
    lastName = forms.CharField()

def 
