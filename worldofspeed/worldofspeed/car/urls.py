from django.urls import path, include


from worldofspeed.car.views import car_details, edit_car, delete_car, create_car, show_all_cars

urlpatterns = [
    path('create/', create_car, name='create-car'),
    path('catalogue/', show_all_cars, name='catalogue'),
    path("<int:pk>/",
         include(
        [path('details/',car_details, name="car-details"),
         path('edit/', edit_car, name="edit-car"),
         path('delete/', delete_car, name="delete-car"),

         ])
         )
]


