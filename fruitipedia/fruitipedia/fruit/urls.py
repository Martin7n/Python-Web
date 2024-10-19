from fruitipedia.fruit.views import create_fruit, edit_fruit, fruit_details, delete_fruit

from django.urls import path, include



urlpatterns = [
    path('create/', create_fruit, name="create-fruit"),
    path('<int:pk>/', include(
            [path('edit/', edit_fruit, name="edit-fruit"),
             path('details/', fruit_details, name="details"),
             path('delete/', delete_fruit, name="delete")

             ]

    )


         )
    # path('edit/', edit_fruit, name="edit-fruit"),
    # path('<int:fruit_id>/', fruit_details, name="fruit-details"),

]