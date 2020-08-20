from django.db import models

# Create your models here.
class project(models.Model):
    title = models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to="perportfolio/images")
    url=models.URLField(blank=True)



    def __str__(self):
        return self.title


class skills(models.Model):
    title=models.CharField(max_length=10)
    progress=models.CharField(max_length=3)

    def __str__(self):
        return self.title

class experience(models.Model):
    title=models.CharField(max_length=100)
    duration=models.CharField(max_length=25)
    description=models.CharField(max_length=300)

    