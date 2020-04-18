from string import *
from random import choice

from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import TopSites


class AddSiteForm(forms.Form):
    name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'id': 'site-name',
                'class': 'inputs',
                'type': 'text',
                'placeholder': 'Nafn síðunnar',
                'title': 'Nafn vefsíðunnar',
            }
        )
    )
    url = forms.CharField(
        required=True,
        initial='https://',
        widget=forms.TextInput(
            attrs={
                'id': 'site-url',
                'class': 'inputs',
                'type': 'text',
                'placeholder': 'www.síðanmín.is',
                'title': 'Vefslóð síðunnar',
                'required': True,
            }
        )
    )
    img = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'id': 'site-img',
                'class': 'inputs',
                'type': 'text',
                'placeholder': 'Slóð á mynd vefsíðunnar',
                'title': 'Slóð á myndmerki vefsíðunnar. Ef ekkert verður valið, munum við finna mynd sjálfkrafa.',
            }
        )
    )
    categories = forms.CharField(
        widget=forms.Select(
            choices=TopSites.CATEGORIES, attrs={
                'id': 'site-cat',
                'class': 'inputs',
                'title': 'Veldu flokk',
            }),
        initial='FAVO',
    )

    def __init__(self, *args, **kwargs):
        super(AddSiteForm, self).__init__(*args, **kwargs)


class RegisterUserForm(UserCreationForm):
    error_messages = {
        'required': 'Þennan reit þarf að fylla út!',
        'password_mismatch': 'Lykilorðin stemma ekki!',
        'password_too_short': 'Lykilorðið er of stutt!',
        'password_too_common': 'Lykilorðið er of algengt!',
    }
    username = forms.CharField(
        required=True,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'id': 'username',
                'class': 'inputs',
                'title': 'Skráðu inn notendanafn',
                # 'placeholder': 'Notendanafn',
                # 'oninvalid': "event.",
                # 'oninput': "setCustomValidity('')",
            }
        )
    )
    email = forms.EmailField(
        required=True,
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                'id': 'email-inp',
                'class': 'inputs',
                'type': 'email',
                'title': 'Sláðu inn netfangið þitt',
                # 'placeholder': 'jon@daemi.is',
            }
        )
    )
    last_name = forms.CharField(
        required=True,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'id': 'l_name-inp',
                'class': 'inputs',
                'type': 'text',
                'title': 'Sláðu inn eftirnafnið þitt',
                # 'placeholder': 'Jónsson',
            }
        )
    )
    first_name = forms.CharField(
        required=True,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'id': 'f_name-inp',
                'class': 'inputs',
                'type': 'text',
                'title': 'Sláðu inn fornafnið þitt',
                # 'placeholder': 'Jón',
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
                # 'placeholder': '********',
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
                # 'placeholder': '',
            }
        )
    )

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     r = User.objects.filter(username=email)
    #     if r.count():
    #         raise ValidationError("Þetta netfang er þegar til!")
    #     return email
    #
    # def clean_password2(self):
    #     pw1 = self.cleaned_data.get('password1')
    #     pw2 = self.cleaned_data.get('password2')
    #     if pw1 and pw2 and pw1 != pw2:
    #         raise ValidationError("Lykilorðin stemma ekki!")
    #     return pw2
    #
    # def save(self, commit=True):
    #     user = User.objects.create_user(
    #         username=self.cleaned_data['email'],
    #         email=self.cleaned_data['email'],
    #         password=self.cleaned_data.get('pw1'),
    #         last_name=self.cleaned_data['last_name'],
    #         first_name=self.cleaned_data['first_name']
    #     )
    #     user.save()
    #     return user

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    # def __init__(self, *args, **kwargs):
    #     super(RegisterUserForm, self).__init__(*args, **kwargs)

    # TODO: Finish register form!
