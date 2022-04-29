from django import forms

from cities.models import City


class RouteForm(forms.Form):
    form_city = forms.ModelChoiceField(label='Откуда',
                                        queryset=City.objects.all(),
                                        widget=forms.Select(attrs={"class": 'form-control js-example-basic-single'}))
    to_city = forms.ModelChoiceField(label='Куда',
                                      queryset=City.objects.all(),
                                      widget=forms.Select(attrs={"class": 'form-control js-example-basic-single'}))
    cities = forms.ModelMultipleChoiceField(label='Через города',
                                            queryset=City.objects.all(),
                                            required=True,
                                            widget=forms.SelectMultiple(
                                                attrs={"class": 'form-control js-example-basic-multiple'}))
    travelling_time = forms.CharField(label='Время в пути', widget=forms.NumberInput(attrs={"class": 'form-control'}))
