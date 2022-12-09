from django import forms
from .models import Profile


class profilecreationsform(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Profile
        fields = ('department', 'date_of_birth')


class usercreateprofile(forms.Form):
    nom = forms.CharField(max_length=100)
    prenom = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)
    email_professional = forms.EmailField()
    numero_du_telephone = forms.CharField()
    institue = forms.CharField()
    accept = forms.BooleanField(label='accept contract',required=True)