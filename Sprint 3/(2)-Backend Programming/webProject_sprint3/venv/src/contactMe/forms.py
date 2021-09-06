from django import forms
from .models import ContactMe

#The code here creates the forms/text input that is connected to the database
class ContactMe_Forms(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(  #name of user
        attrs={ #For CSS
            'class': 'form-text',
            'placeholder': 'Name'
        }
    ))

    email = forms.CharField(widget=forms.TextInput(  #email of user
        attrs={ #For CSS
            'class': 'form-text',
            'placeholder': 'Email'
        }
    ))
    
    message = forms.CharField(widget=forms.Textarea( #message of user
        attrs={ #For CSS
            'class': 'form-textMessage',
            'placeholder': 'Message'
        }
    ))

    class Meta:
        model = ContactMe
        fields = [
            'name',
            'email',
            'message'
        ]