from django import forms

# class AddNewLog(forms.Form):
#     content = forms.CharField(help_text="Enter your content here")

from .models import Log

class LogForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}))
    class Meta:
        model = Log
        fields = ['content',]
