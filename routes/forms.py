from django import forms

from cities.models import City
from routes.models import Route


class RouteForm(forms.ModelForm):
    cities = forms.ModelMultipleChoiceField(label='Через города', required=False, queryset=City.objects.all(),
                                            widget=forms.SelectMultiple(attrs={'class': 'form-control js-example-basic-multiple'}))

    class Meta:
        model = Route
        fields = ('from_city', 'to_city', 'cities', 'travel_times')

        widgets = {
            'from_city': forms.Select(attrs={'class': 'form-control js-example-basic-single'}),
            'to_city': forms.Select(attrs={'class': 'form-control js-example-basic-single'}),
            'travel_times': forms.NumberInput(attrs={'class': 'form-control'})
        }
