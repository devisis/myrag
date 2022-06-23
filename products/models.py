from django.db import models
from django.contrib.auth.models import User




class Product(models.Model):
    """Model for Product"""
    material_choices = (
    ("Sil", "Silk"),
    ("Vel", "Velvet"),
    ("Sat", "Satin"),
    )

    color_choices = (
    ("R","Red"),
    ("G", "Green"),
    ("B", "Blue"),
    )

    name = models.CharField(max_length=50)
    material = models.CharField(max_length=50, choices=material_choices, default="Silk")
    primary_color = models.CharField(max_length=50, choices=color_choices, default="Red")
    secondary_color = models.CharField(max_length=50, choices=color_choices, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    """Model for Reviews"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=200, blank=True)
    when_created = models.DateTimeField()
