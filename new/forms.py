from django import forms
from django.core.exceptions import ValidationError
from .models import Todo

#
# class TodoForm(forms.Form):
#     nom = forms.CharField(label="nomi")
#     vaqt = forms.CharField(label="vaqt")
#     stats = forms.BooleanField()
#     tarixi = forms.IntegerField()

# class TodoForm(forms.ModelForm):
#     class Meta:
#         model = Todo
#         fields = ('nom', 'vaqt', 'tarixi', 'stats')
