from django import forms
from django.forms import fields, widgets
from .models import User

class Registration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['id','name','email','roll','year','contact']

        widgets = {

            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'roll': forms.TextInput(attrs={'class':'form-control'}),
            'year': forms.NumberInput(attrs={'class':'form-control'}),
            'contact': forms.NumberInput(attrs={'class':'form-control'})

        }