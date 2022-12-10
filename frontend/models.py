from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    anons = models.TextField()

    def __str__(self):
        return self.title