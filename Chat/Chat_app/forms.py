from django import forms
from .models import Messages

class MessagesForm(forms.ModelForm):
    class Meta:
        fields = ('message',)
        model = Messages