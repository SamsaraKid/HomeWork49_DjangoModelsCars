from django import forms


class CarForm(forms.Form):
    mark = forms.CharField(max_length=20, initial='q')
    producer = forms.CharField(max_length=20, initial='q')
    year = forms.IntegerField(initial='1')
    num = forms.CharField(max_length=20, initial='q')