from django.db import models

# Create your models here.
class Review(models.Model):
    username = models.CharField(max_length=200)
    review_text = models.TextField()
    rating = models.IntegerField()