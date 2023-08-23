from django.urls import path
from .views import avtouser, autorisation_user, registration_user, register, login

urlpatterns = [
    path('', avtouser),
    path('autorisation/', autorisation_user, name='autorisation'),
    path('registration/', registration_user, name='registration'),
    path('register/', register, name='register'),
    path('login/', login, name='login')
]
