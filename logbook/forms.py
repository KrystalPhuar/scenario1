from django import forms
from .models import Log
from logbook import models

class LogForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}))
    class Meta:
        model = Log
        fields = ['content', 'section']
