from django import forms
from django.core.exceptions import ValidationError
from account.models import User


class SignUpForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    profile_image = forms.ImageField(required=False)
    short_description = forms.CharField(required=False)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError(f'The user name ({username}) has already been in use...')
        return username

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            self.add_error("password2", "please check password...")

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password1'],
            profile_image=self.cleaned_data.get('profile_image'),
            short_description=self.cleaned_data.get('short_description'),
        )
        # print(user)
        return user


class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        widget=forms.TextInput(attrs={"placeholder": "username (more than 3 digits)"}),
    )
    password = forms.CharField(
        min_length=4,
        widget=forms.PasswordInput(attrs={"placeholder": "password (more than 4 digits)"}),
    )
