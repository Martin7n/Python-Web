from django.shortcuts import render, redirect

from fruitipedia.fruit.forms import CreateFruitForm, EditFruitForm, DeleteFruitForm
from fruitipedia.fruit.models import Fruit
from fruitipedia.user_profile.models import Profile


# Create your views here.



def index(request):
    profile = Profile.objects.first()
    context = {
        "profile": profile
    }
    return render(request, 'index.html', context)

def dashboard(request):
    fruits = Fruit.objects.all()
    profile = Profile.objects.first()
    context = {
        "fruits": fruits,
        "profile": profile
    }

    return render(request, 'dashboard.html', context)

def create_fruit(request):
    profile = Profile.objects.first()
    form = CreateFruitForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.owner = profile
            form.save()
            return redirect("dashboard")

    context = {
        "form": form,
        "profile": profile
    }

    return render(request, 'create-fruit.html', context)


def fruit_details(request, pk):
    profile = Profile.objects.first()
    fruit = Fruit.objects.get(pk=pk)

    context = {
        "profile": profile,
        'fruit': fruit
    }

    return render(request, "details-fruit.html", context)





def edit_fruit(request, pk):
    profile = Profile.objects.first()
    fruit = Fruit.objects.get(id=pk)

    form = EditFruitForm(instance=fruit)

    if request.method == 'POST':
        form = EditFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        "profile": profile,
        "fruit":fruit,
        "form": form
    }

    return render(request, 'edit-fruit.html', context)


def delete_fruit(request, pk):
    profile = Profile.objects.first()
    fruit = Fruit.objects.get(id=pk)

    form = DeleteFruitForm(instance=fruit)
    if request.method == 'POST':
        fruit.delete()
        return redirect('dashboard')

    context = {
        "profile": profile,
        "fruit":fruit,
        "form": form
    }

    return render(request, 'delete-fruit.html', context)
