

from django.urls import path, include


from fruitipedia.user_profile.views import profile_details, edit_profile, delete_profile, create_profile

urlpatterns = [path("details/", profile_details, name="profile_details"),
               path("create-profile/", create_profile, name="create-profile"),
               path("<int:pk>/", include(
                   [path("edit-profile/", edit_profile, name="edit-profile"),
                    path("delete-profile/", delete_profile, name="delete-profile")
                    ])
                    )
               ]


    # • http://localhost:8000/ - Index page
    # • http://localhost:8000/dashboard/ - Dashboard page
    # • http://localhost:8000/fruit/create/ - Fruit create page
    # • http://localhost:8000/fruit/<fruitId>/details/ - Fruit details page
    # • http://localhost:8000/fruit/<fruitId>/edit/ - Fruit edit page
    # • http://localhost:8000/fruit/<fruitId>/delete/ - Fruit delete page
    # • http://localhost:8000/profile/create/ - Profile create page
    # • http://localhost:8000/profile/details/ - Profile details page
    # • http://localhost:8000/profile/edit/ - Profile edit page
    # • http://localhost:8000/profile/delete/ - Profile delete page