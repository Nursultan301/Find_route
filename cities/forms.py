from django import forms

from cities.models import City


class CityForm(forms.ModelForm):
    name = forms.CharField(label='Город', widget=forms.TextInput(attrs={
        "class": "form-control",
        'placeholder': 'Введите называние города ',
    }))

    class Meta:
        model = City
        fields = ('name',)
