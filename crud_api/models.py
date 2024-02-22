from django.db import models

# Create your models here.

class Review(models.Model):
    rating = models.IntegerField()
    review = models.CharField(max_length=300)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publication_date = models.DateField() 
    review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True, blank=True, related_name="reviews")
    


