from django import forms
from django.contrib.auth import authenticate
from django.core.validators import ValidationError
from account.models import User
import re
user_degree = (
        ("Foundation","foundation"),
        ('Associate','associate'),
        ('Bachelors','bachelors'),
        ('Masters','masters'),
        ('PHD','phd')
    )

class LoginForm(forms.Form):
    auth = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control","placeholder":"YOUR EMAIL OR USERNAME"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control","placeholder":"YOUR PASSWORD"}))

    def clean(self):
        auth = self.cleaned_data['auth']
        password = self.cleaned_data['password']
        user = authenticate(username = auth ,password = password)
        if user is None:
            raise ValidationError("please enter correct username and password" , code="login_pass_user")


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))

    class Meta:
        model = User
        fields = ['username','email','degree']
        widgets ={
            'username':forms.TextInput(attrs={'class':"form-control"}),
            'email':forms.EmailInput(attrs={'class':"form-control"}),
            'degree':forms.Select(attrs={'class':"form-control form-select dept-select"})
        }


    def clean_password1(self):
        pass1 = self.cleaned_data.get('password1')
        if len(pass1)<12 :
            raise ValidationError('less than 12 employees',code='12_pass1')
        if not re.match(r'^[a-zA-Z0-9@#%]+$',pass1):
            raise ValidationError('the password is weak',code='pass_weak')
        return pass1

    def clean(self):
        cleaned_data = super().clean()
        pass1 = self.cleaned_data.get('password1')
        pass2 = self.cleaned_data.get('password2')
        if pass1 != pass2 :
            raise ValidationError('please enter same password',code='same pass1,2')
        return cleaned_data


class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('degree','image','username','email','password')
        widgets = {
            'username': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.EmailInput(attrs={'class': "form-control"}),
            'degree': forms.Select(attrs={'class': "form-control form-select dept-select"}),
            'password':forms.PasswordInput(attrs={'class': "form-control"})
        }

    def clean_password(self):
        pass1 = self.cleaned_data.get('password1')
        if len(pass1)<12 :
            raise ValidationError('less than 12 employees',code='12_pass1')
        if not re.match(r'^[a-zA-Z0-9@#%]+$',pass1):
            raise ValidationError('the password is weak',code='pass_weak')
        return pass1

