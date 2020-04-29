from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.forms import widgets
from django.contrib.auth.models import User


class EditUserForm(UserChangeForm):
    email = forms.EmailField(
        required=False,
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                'id': 'email-inp',
                'class': 'inputs',
                'type': 'email',
                # 'title': 'Sláðu inn netfangið þitt',
                # 'placeholder': 'jon@daemi.is',
            }
        )
    )
    last_name = forms.CharField(
        required=False,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'id': 'l_name-inp',
                'class': 'inputs',
                'type': 'text',
                # 'title': 'Sláðu inn eftirnafnið þitt',
                # 'placeholder': 'Jónsson',
            }
        )
    )
    first_name = forms.CharField(
        required=False,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'id': 'f_name-inp',
                'class': 'inputs',
                'type': 'text',
                # 'title': 'Sláðu inn fornafnið þitt',
                # 'placeholder': 'Jón',
            }
        )
    )

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class ResetPWForm(PasswordChangeForm):
    old_password = forms.CharField(
        required=True,
        max_length=254,
        widget=forms.PasswordInput(
            attrs={
                'id': 'old_pw',
                'class': 'inputs',
                'type': 'password',
            }
        )
    )
    password1 = forms.CharField(
        required=True,
        max_length=254,
        widget=forms.PasswordInput(
            attrs={
                'id': 'pw1',
                'class': 'inputs',
                'type': 'password',
                'title': 'Sláðu inn lykilorð',
            }
        )
    )
    password2 = forms.CharField(
        required=True,
        max_length=254,
        widget=forms.PasswordInput(
            attrs={
                'id': 'pw2',
                'class': 'inputs',
                'type': 'password',
            }
        )
    )

    class Meta:
        model = User
        fields = ('password1', 'password2')
