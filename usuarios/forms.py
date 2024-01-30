from django import forms
from django.contrib.auth.models import User
from . import models

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = models.Usuarios
        fields = '__all__'
        exclude = ('usuario',)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username','email', 'password')
        
    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data