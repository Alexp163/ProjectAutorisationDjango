from django.db import models

class MyBase(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)