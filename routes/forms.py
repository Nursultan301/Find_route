from django import forms

from cities.models import City
from routes.models import Route


class RouteForm(forms.ModelForm):
    cities = forms.ModelMultipleChoiceField(label='Через города', queryset=City.objects.all(),
                                            widget=forms.SelectMultiple(attrs={'class': 'form-control'}))

    class Meta:
        model = Route
        fields = ('from_city', 'to_city', 'cities', 'travel_times')

        widgets = {
            'from_city': forms.Select(attrs={'class': 'form-control'}),
            'to_city': forms.Select(attrs={'class': 'form-control'}),
            'travel_times': forms.NumberInput(attrs={'class': 'form-control'})
        }
