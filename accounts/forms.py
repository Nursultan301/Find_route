from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите логин"}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Введите пароль"}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            qs = User.objects.filter(username=username)
            if not qs.exists():
                raise forms.ValidationError('Такого пользователя нет')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Неверный пароль')
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Данный пользователь не активен')
        return super().clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите логин"}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Введите пароль"}))
    password2 = forms.CharField(label='Подтверждение пароля',
                               widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Подтверждение пароля"}))

    class Meta:
        model = User
        fields =('username',)

        def clean_password2(self):
            data = self.cleaned_data
            if data['password'] != data['password2']:
                raise forms.ValidationError('пароли не совпадает')
            return data['password2']
