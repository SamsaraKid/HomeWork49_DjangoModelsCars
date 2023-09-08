from django.shortcuts import render, redirect
from .myforms import CarForm
from .models import Car


def index(req):
    form = CarForm()
    db = Car.objects.values_list()
    return render(req, 'index.html', context={'form': form, 'database': db})


def add(req):
    if req.POST:
        car = Car()
        car.mark = req.POST.get('mark')
        car.producer = req.POST.get('producer')
        car.year = req.POST.get('year')
        car.num = req.POST.get('num')
        car.save()
        return redirect('index')


def delete(req, id):
    car = Car.objects.get(id=id)
    car.delete()
    return redirect('index')

