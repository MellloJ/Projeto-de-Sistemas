from django import forms

class signupForm(forms.Form):
    email
    password
    cpf
    name = Form.CharField(max_lenght="50")
    lastName = Form.