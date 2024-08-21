from django import forms 
from .models import Company


class UpdateCompamy(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ('user' , )
    
