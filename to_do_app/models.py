from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.







class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=100)
    add_date = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.task
    

