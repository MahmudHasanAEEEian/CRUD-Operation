from django import forms
from .models import Person

#Model forms creation

class PersonCreateForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'