from django import forms
from .models import Work

class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Work
        exclude = ('user' , 'company' ,)


class UpdateJobForm(forms.ModelForm):
    class Meta:
        model = Work
        exclude = ('user' , 'company' ,)