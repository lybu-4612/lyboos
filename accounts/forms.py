from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password'
    }))
    
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))
    
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'password' ,'phonenumber' ]
        
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs )
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter FirstName'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter LastName'
        self.fields['phonenumber'].widget.attrs['placeholder'] = 'Enter Phonenumber'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter EmailAddress'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'