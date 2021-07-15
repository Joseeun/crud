from django.db import models

class UserInformation(models.Model):
    age = models.CharField(max_length=50)
    address = models.CharField(max_length=500)