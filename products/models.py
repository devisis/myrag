from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Product(models.Model):
    """Model for Product"""

    MATERIAL_CHOICES = (
        ("Silk", "Silk"),
        ("Velvet", "Velvet"),
        ("Satin", "Satin"),
    )

    STYLE_CHOICES = (
        ("Default", "Default"),
        ("Camo", "Camo"),
        ("Bandana", "Bandana"),
    )

    category = models.ForeignKey(
        'Category', blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    style = models.CharField(
        max_length=200, choices=STYLE_CHOICES, default="Default")
    material = models.CharField(
        max_length=200, choices=MATERIAL_CHOICES, default="Silk")
    color = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    """Model for Category"""

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
