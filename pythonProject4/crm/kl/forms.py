from .models import listofcompanies
from django.forms import ModelForm, TextInput


class listofcompaniesForm(ModelForm):
    class Meta:
        model = listofcompanies
        fields = ['name', 'city', 'industry']
        widgets = {
            'name': TextInput(attrs={
                'clas': 'form_control',
                'placeholder': "Введіть назву"

        }),
            'city': TextInput(attrs={
                'clas': 'form_control',
                'placeholder': "Введіть місто"
        }),
            'industry': TextInput(attrs={
                'clas': 'form_control',
                'placeholder': "Введіть галузь"
            }),
        }
