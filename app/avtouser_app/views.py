from django.shortcuts import render

from avtouser_app.models import MyBase


def avtouser(request):
    return render(request, 'avtouser_app/index.html')


def autorisation_user(request):
    return render(request, "avtouser_app/autorisation.html")


def registration_user(request):
    return render(request, "avtouser_app/registration.html")

def register(request):
    login = request.POST.get('login')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    if password1 != password2:
        return render(request, "avtouser_app/registration.html")
    MyBase.objects.get_or_create(login=login, password=password1)
    return render(request, "avtouser_app/index.html")