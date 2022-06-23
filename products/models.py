from django.db import models
from django.contrib.auth.models import User




class Product(models.Model):
    """Model for Product"""
    MATERIAL_CHOICES = (
    ("Sil", "Silk"),
    ("Vel", "Velvet"),
    ("Sat", "Satin"),
    )

    COLOR_CHOICES = (
    ("R","Red"),
    ("G", "Green"),
    ("B", "Blue"),
    )

    STYLE_CHOICES = (
    ("def", "Default"),
    ("TT", "Two Tone"),
    ("Cam", "Camo"),
    ("Ban", "Bandana"),
    )

    style = models.CharField(max_length=50, choices=material_choices, default="Default")
    material = models.CharField(max_length=50, choices=material_choices, default="Silk")
    primary_color = models.CharField(max_length=50, choices=color_choices, default="Red")
    secondary_color = models.CharField(max_length=50, choices=color_choices, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name

# class FAQ(models.Model):
#     question = 
#     description =

# class Newsletter(models.Model):

# class Review(models.Model):
#     """Model for Reviews"""
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     username = models.ForeignKey(User, on_delete=models.CASCADE)
#     message = models.TextField(max_length=200, blank=True)
#     when_created = models.DateTimeField()
