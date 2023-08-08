from django.urls import path
from .views import avtouser, autorisation_user, registration_user, register

urlpatterns = [
    path('', avtouser),
    path('autorisation/', autorisation_user),
    path('registration/', registration_user),
    path('register/', register, name='register')
]
