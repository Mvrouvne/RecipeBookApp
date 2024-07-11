from django.db import models

# Create your models here.

class   Books(models.Model):
    title = models.CharField(max_length=50)
    ingredients = models.TextField()
    instructions = models.TextField()
    preparation_time = models.CharField(max_length=10)

    def __str__(self):
        return self.title