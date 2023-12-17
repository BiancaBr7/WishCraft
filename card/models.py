from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Wish(models.Model):
    sender_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, default='*Title Of Your Wish*')
    receiver = models.CharField(max_length=100, default='*Your Receiver*')
    message = models.TextField()
    password = models.CharField(max_length=20)
    signature = models.CharField(max_length = 100, blank=True, default='Happy Christmas,')