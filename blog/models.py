from django.db import models
import datetime
# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(default=datetime.date.today)
    description = models.TextField(max_length=600)


    def __str__(self):
        return self.title
