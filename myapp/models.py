from django.db import models
from datetime import datetime

# Create your models here.

class weather(models.Model):
    city = models.CharField(max_length=100)
    time = models.DateTimeField(default=datetime.now, blank=True)


    
