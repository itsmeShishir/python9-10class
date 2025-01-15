# login and register form for user
from django import forms
from  .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2','phone_number', 'role')

class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'phone_number', 'role')

class UserChangePassword(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if new_password != confirm_password:
            raise forms.ValidationError('Password does not match')
        return cleaned_data

