from django import forms

from trains.models import Train


class TrainForm(forms.ModelForm):
    name = forms.CharField(label='Номер поезда', widget=forms.TextInput(attrs={"class": 'form-control'}))
    travel_time = forms.CharField(label='Номер поезда', widget=forms.TextInput(attrs={"class": 'form-control'}))
    form_city = forms.CharField(label='Номер поезда', widget=forms.Select(attrs={"class": 'form-control'}))
    to_city = forms.CharField(label='Номер поезда', widget=forms.Select(attrs={"class": 'form-control'}))

    class Meta:
        model = Train
        fields = '__all__'
