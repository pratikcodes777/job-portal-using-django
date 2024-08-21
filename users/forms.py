from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
User = get_user_model()

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1' , 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        User = get_user_model()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered.')
        return email
