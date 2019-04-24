from django.db import models
from django.contrib.auth.models import User

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField
    phone = models.PositiveSmallIntegerField
    available = models.BooleanField
