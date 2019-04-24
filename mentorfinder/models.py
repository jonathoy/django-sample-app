from django.db import models
from django.contrib.auth.models import User

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    phone = models.PositiveSmallIntegerField()
    available = models.BooleanField()
