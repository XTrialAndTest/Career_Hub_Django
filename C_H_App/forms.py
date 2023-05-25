from .models import *
from django import forms


class Jobform(forms.ModelForm):
    class Meta:
        model = Job_Model
        fields = '__all__'
