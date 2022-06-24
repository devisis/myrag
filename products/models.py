from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Product(models.Model):
    """Model for Product"""
    name = models.CharField(max_length=200)
    style = models.CharField(max_length=200)
    material = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    secondary_color = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    featured_image = CloudinaryField('image', default='placeholder')
    slug = models.SlugField(max_length=200, unique=True, editable=False)
    description = models.TextField()

    def __str__(self):
        return self.name
