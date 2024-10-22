from worldofspeed.car.models import Car
from worldofspeed.user_profile.models import Profile


def get_profile():
    profile = Profile.objects.first()
    return profile

def get_all_cars():
    cars = Car.objects.all()
    return cars

def tot_price():
    profile = get_profile()
    cars = Car.objects.select_related('owner')
    total = sum([x.price for x in cars])
    return total


