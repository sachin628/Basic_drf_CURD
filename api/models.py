from django.db import models

# Create your models here.
class Items(models.Model):
    category =models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)


    def __str__(self):
        return self.name