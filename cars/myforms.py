from django import forms


class CarForm(forms.Form):
    mark = forms.CharField(max_length=20)
    producer = forms.CharField(max_length=20)
    year = forms.IntegerField()
    num = forms.CharField(max_length=20)