from django.db import models

# Create your models here.
class News(models.Model):
    approved = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    anons = models.TextField()

    @property
    def number_of_subscribers(self):
        return 100

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:10]