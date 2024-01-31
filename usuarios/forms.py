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
        
        """
        usuario_data = data['username']
        password_data = data['password']
        email_data = data['email']
        """
        usuario_data = cleaned.get('username')
        email_data = cleaned.get('email')
        password_data = cleaned.get('password')
        password2_data = cleaned.get('password2')
        
        usuario_db = User.objects.filter(username=usuario_data).first()
        email_db = User.objects.filter(email=email_data).first()
        
        error_msg_user_exists = 'Usário já existe'
        error_msg_email_exists = 'Email já em uso'
        error_msg_password_match = 'As senhas são diferentes'
        error_msg_password_short = 'A senha deve ter mais de 5 caracteres'

        #usuários logados: atualizar usuário
        if self.usuario:
            if usuario_db:
                if usuario_data != usuario_db.username:
                    validation_error_msgs['username'] = error_msg_user_exists

            if email_db:
                if email_data != email_db.email:
                    validation_error_msgs['email'] = error_msg_email_exists

            if password_data:
                if password_data != password2_data:
                    validation_error_msgs['password'] = error_msg_password_match
                    validation_error_msgs['password2'] = error_msg_password_match

                if len(password_data) < 6:
                    validation_error_msgs['password'] = error_msg_password_short
        #usuários não logados: cadastrar
        else:
            pass
        
        if validation_error_msgs:
            raise(forms.ValidationError(validation_error_msgs))