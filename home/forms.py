from dataclasses import field
from email.policy import default
from multiprocessing import AuthenticationError
from urllib import request
from django.forms import ModelForm
from django import forms
# from .models import users_info
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.views.generic import UpdateView
from django.urls import path, reverse_lazy
from .models import takePart,contactUs


username_validator = UnicodeUsernameValidator()


class users_input (UserCreationForm):
    
    first_name = forms.CharField(max_length=12, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control p-2 mt-2 text-center '}),
                                 error_messages={'required': 'يجب إدخال الاسم الأول'})
    last_name = forms.CharField(max_length=12, required=True,
                                widget=(forms.TextInput(attrs={'class': 'form-control p-2 mt-2 text-center '})),
                                error_messages={'required': 'يجب إدخال اسم العائلة'})
    email = forms.EmailField(max_length=50,
                             widget=(forms.TextInput(attrs={'class': 'form-control p-2 mt-2 text-center '})),
                             error_messages={'required': 'يجب إدخال البريد الإلكتروني'})

    password1 = forms.CharField(
        widget=(forms.PasswordInput(
            attrs={'class': 'form-control p-2 mt-2 text-center '})))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control p-2 mt-2 text-center '}))

    username = forms.CharField(
        max_length=150,
        validators=[username_validator],
        widget=forms.TextInput(
            attrs={'class': 'form-control p-2 mt-2 text-center '}),
        error_messages={'unique': (
            "الاسم مُستخدم بالفعل")},
    )
    
    
    def __init__(self, *args, **kwargs):
        super(users_input, self).__init__(*args, **kwargs)

        self.fields['username'].label = 'اسم المستخدم (باللغة الإنجليزية) '
        self.fields['email'].label = 'البريد الإلكتروني'
        self.fields['password1'].label = 'كلمة المرور '
        self.fields['password2'].label = 'تحقق من كلمة المرور'
        self.fields['first_name'].label = 'الاسم الأول'
        self.fields['last_name'].label = 'اسم العائلة'

        for field in self.fields:
            self.fields[field].help_text = ''

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',
                  'first_name', 'last_name']


class updateProfile(forms.ModelForm):
    first_name = forms.CharField(max_length=12, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control p-2 mt-2 text-center '}))
    last_name = forms.CharField(max_length=12, required=True,
                                widget=(forms.TextInput(attrs={'class': 'form-control p-2 mt-2 text-center '})))
    email = forms.EmailField(max_length=50,
                             widget=(forms.TextInput(attrs={'class': 'form-control p-2 mt-2 text-center '})))

    username = forms.CharField(
        disabled=True,
        max_length=150,
        validators=[username_validator],
        # error_messages={'unique': _(
        #     "A user with that username already exists.")},
        widget=forms.TextInput(
            attrs={'class': 'form-control p-2 mt-2 text-center '})
    )

    def __init__(self, *args, **kwargs):
        super(updateProfile, self).__init__(*args, **kwargs)

        self.fields['username'].label = 'اسم المستخدم (باللغة الإنجليزية) '
        self.fields['email'].label = 'البريد الإلكتروني'
        self.fields['first_name'].label = 'الاسم الأول'
        self.fields['last_name'].label = 'اسم العائلة'

        for field in self.fields:
            self.fields[field].help_text = ''

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class loginForm (AuthenticationForm):

    password = forms.CharField(
        widget=(forms.PasswordInput(
            attrs={'class': 'form-control p-2 mt-2 text-center '})))

    username = forms.CharField(
        max_length=150,
        validators=[username_validator],
        # error_messages={'unique': _(
        #     "A user with that username already exists.")},
        widget=forms.TextInput(
            attrs={'class': 'form-control p-2 mt-2 text-center '})
    )

    def __init__(self, *args, **kwargs):
        super(loginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "اسم المستخدم (باللغة الإنجليزية)"
        self.fields['password'].label = 'كلمة المرور '

        for field in self.fields:
            self.fields[field].help_text = ''


class takePartF(forms.ModelForm):
    subject = forms.CharField(max_length=100, widget=(forms.TextInput(
        attrs={'class': 'form-control p-2 text-center ', 'placeholder': ' عنوان الفقرة'})))

    descripion = forms.CharField(widget=(forms.Textarea(
        attrs={'class': 'form-control p-2', 'rows': '4'})))
    
    document = forms.FileField(widget=(forms.FileInput(
        attrs={'class': 'form-control p-2 bg-transparent'})))
    
    user = forms.CharField(max_length=100, required=False, widget=(forms.TextInput(
        attrs={'class': 'd-none '})))
    
    class Meta:
        model = takePart
        fields = ['subject', 'descripion', 'document','user']

class contactus(forms.ModelForm):
    email = forms.EmailField(max_length=50, required=False,
                             widget=(forms.TextInput(attrs={'class': 'd-none '})))

    message = forms.CharField(widget=(forms.Textarea(
        attrs={'class': 'form-control p-2', 'rows': '4'})))
    
    user = forms.CharField(max_length=100, required=False, widget=(forms.TextInput(
        attrs={'class': 'd-none '})))
    
    class Meta:
        model = contactUs
        fields = ['message', 'email','user']