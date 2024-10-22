from django.shortcuts import render, redirect

from worldofspeed.car.models import Car
from worldofspeed.core.utils import get_profile, get_all_cars

from worldofspeed.car.forms import CreateCarForm, EditCarForm, CarDelForm


# Create your views here.


def index(request):
    profile = get_profile()
    cars = get_all_cars()

    context ={
        "profile":profile,
        "cars":cars
    }
    return render(request,"index.html", context)

def car_details(request, pk):
    car = Car.objects.get(pk=pk)
    profile = get_profile()

    context = {
        "profile":profile,
         "car": car}

    return render(request,"car-details.html", context)


def create_car(request):
    form = CreateCarForm()
    profile = get_profile()

    #TODO add the PK of the profile!
    if request.method == 'POST':
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.instance.owner_id = profile.pk

            form.save()
            return redirect("index")

    context = {
        "profile": get_profile,
        "form": form}
    return render(request, 'car-create.html', context)

def edit_car(request, pk):
    profile = get_profile()
    car = Car.objects.get(pk=pk)
    form = EditCarForm(instance=car)

    if request.method == 'POST':
        form = EditCarForm(request.POST, instance=car)
        print(form)
        if form.is_valid():
            # form.instance.owner_id = get_profile().pk
            form.save()
            return redirect('catalogue')

    context = {
        "profile": profile,
        "car": car,
        "form": form
    }

    return render(request,"car-edit.html", context)

def delete_car(request, pk):
    profile = get_profile()
    car = Car.objects.get(pk=pk)

    form = CarDelForm(instance=car)
    if request.method == "POST":
        car.delete()
        return redirect('index')

    context = {
        "profile": profile,
        "car": car,
        "form":form
    }

    return render(request,"car-delete.html", context)


def show_all_cars(request):
    profile = get_profile()
    cars = get_all_cars()
    first_car = Car.objects.first()
    context = {
        "profile": profile,
        "cars": cars,
        "first_car": first_car
    }
    return render(request,"catalogue.html", context)