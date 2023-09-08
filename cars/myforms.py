from django import forms


class CarForm(forms.Form):
    mark = forms.CharField(label='Марка', max_length=20)
    producer = forms.CharField(label='Производитель', max_length=20)
    year = forms.IntegerField(label='Год')
    num = forms.CharField(label='Номер', max_length=20)