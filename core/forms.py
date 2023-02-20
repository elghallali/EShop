from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm, PasswordResetForm

from django.contrib.auth.models import User

from .models import Customer, PostMessageContact



class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control mt-2'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class': 'form-control mt-2'}))



class CustomerRegistrationForm(UserCreationForm):

    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control mt-2'}))

    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class': 'form-control mt-2'}))

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control mt-2'}))

    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class': 'form-control mt-2'}))


    class Meta:

        model = User

        fields = ['username', 'email', 'password1', 'password2']


class MyPasswordChangeForm(PasswordChangeForm):

    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'autofocus': 'True', 'class': 'form-control mt-2'}))

    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control mt-2'}))

    new_password2 = forms.CharField(label='Confirm New Password',widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control mt-2'}))



class MyPasswordResetForm(PasswordResetForm):

    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class': 'form-control mt-2'}))


class MySetPasswordForm(SetPasswordForm):

    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control mt-2'}))

    new_password2 = forms.CharField(label='Confirm New Password',widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control mt-2'}))


class CustomerProfileForm(forms.ModelForm):

    class Meta:

        model = Customer

        fields = ('name', 'locality', 'city', 'mobile', 'state', 'zipcode')

        widgets={

            'name':forms.TextInput(attrs={'class': 'form-control mt-2'}),

            'locality':forms.TextInput(attrs={'class': 'form-control mt-2'}),

            'city':forms.TextInput(attrs={'class': 'form-control mt-2'}),

            'mobile':forms.NumberInput(attrs={'class': 'form-control mt-2'}),

            'state':forms.Select(attrs={'class': 'form-control mt-2'}),

            'zipcode':forms.NumberInput(attrs={'class': 'form-control mt-2'}),

        }



class PostMessageContactForm(forms.ModelForm):

    class Meta:

        model = PostMessageContact
        fields = ('name', 'email', 'content')

        widgets={

            'name':forms.TextInput(attrs={'placeholder':'Your name', 'aria-label':'Your name','class': 'form-control mt-2'}),

            'email':forms.EmailInput(attrs={'placeholder':'Your email', 'aria-label':'Your email','class': 'form-control mt-2'}),

            'content':forms.Textarea(attrs={'cols':80, 'rows':5, 'class': 'form-control mt-2'}),

        }

