from django import forms

from cities.models import City


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('title', )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Введите название города'
                                            })
        }
        labels = {
            'title': 'Город'
        }
