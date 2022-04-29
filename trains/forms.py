from django import forms

from trains.models import Train


class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = '__all__'
        
        widgets = {
            'name': forms.TextInput(attrs={"class": 'form-control'}),
            'travel_time': forms.NumberInput(attrs={"class": 'form-control'}),
            'from_city': forms.Select(attrs={"class": 'form-control'}),
            'to_city': forms.Select(attrs={"class": 'form-control'}),
        }
