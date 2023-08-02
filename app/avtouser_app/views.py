from django.shortcuts import render


def avtouser(request):
    return render(request, 'avtouser_app/index.html')


def autorisation_user(request):
    return render(request, "avtouser_app/autorisation.html")


def registration_user(request):
    return render(request, "avtouser_app/registration.html")
