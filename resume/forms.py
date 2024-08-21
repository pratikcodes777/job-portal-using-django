from django import forms
from .models import Resume


class UpdateResume(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = ('user' , )