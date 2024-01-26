from .models import Task
from django import forms

class taskform(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']