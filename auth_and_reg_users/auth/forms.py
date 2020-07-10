from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(help_text= None, label = 'Имя пользователя\n')
    password1 = forms.CharField(help_text=None,
                                label='Придумайте пароль',
                                widget=forms.PasswordInput())
    password2 = forms.CharField(help_text=None,
                                label='Подтвердите пароль',
                                widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ("username", "password1", "password2", )

class AuthForm(AuthenticationForm):
    username = UsernameField(label = 'Имя пользователя\n')
    password = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ("username", "password", )