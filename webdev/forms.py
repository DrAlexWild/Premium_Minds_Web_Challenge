from django import forms
from django.forms import ModelForm

from .models import Utilizador

class Utilizador_Form(ModelForm):
    palavra_passe = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Utilizador
        fields = '__all__'

        widgets = {'nome': forms.HiddenInput()}
