from django.urls import path
from .views import avtouser, autorisation_user, registration_user


urlpatterns = [
    path('', avtouser),
    path('autorisation/', autorisation_user),
    path('registration/', registration_user),

]
