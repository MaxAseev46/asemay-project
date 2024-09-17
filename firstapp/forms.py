from django import forms
class UserForm(forms.Form):
    name = forms.CharField(label="Имя клиента", min_length=3)
    age = forms.IntegerField(label="Возраст клиента", min_value=1, max_value=100)
    weight = forms.DecimalField(min_value=3, max_value=200, decimal_places=2)
    email = forms.EmailField(label="Электронный адрес")
    reklama = forms.BooleanField(label="Согласны получать рекламу", required=False)
