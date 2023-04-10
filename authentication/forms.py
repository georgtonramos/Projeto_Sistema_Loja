from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.utils.translation import gettext_lazy as _



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))
    error_messages = {
        'invalid_login': _(
            "Por favor, insira um nome de usuário e senha corretos. "
            "Observe que ambos os campos diferenciam maiúsculas de minúsculas."
        ),
        'inactive': _("Esta conta está inativa."),
    }
class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
