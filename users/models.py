from django.db import models


class Profile(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    birthdate = models.DateField()

# Create your models here.
