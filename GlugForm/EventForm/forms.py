from django import forms
from .models import Person
from django.forms import ModelForm

class Event_registration_form(ModelForm):
    email=forms.EmailField()#widget=forms.EmailInput(attrs={'style': 'border-color: #ff9933;'}))
    name=forms.CharField()
    usn=forms.CharField()
    dept=forms.ChoiceField(choices=(('CSE','CSE'),('ISE','ISE'),('ECE','ECE'),('TCE','TCE'),('EEE','EEE'),('ME','ME'),('CV','CV'),('Basic Science','Basic Science')))
    
    class Meta:
        model=Person
        fields='__all__'