from django import forms
from django.contrib.auth.models import User
from . import models

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = '__all__'
        exclude = ('usuario',)

class UserForm(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Senha'
    )
    
    password2 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Repita sua senha'
    )
    
    
    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.usuario = usuario
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username','email', 'password', 'password2')
        
    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data
        validation_error_msgs = {}
        
        #usuários logados: atualizar usuário
        if self.usuario:
            print('LOGADO')
        #usuários não logados: cadastrar
        else:
            pass
        
        if validation_error_msgs:
            raise(forms.ValidationError(validation_error_msgs))