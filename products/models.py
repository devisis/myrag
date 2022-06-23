from django.db import models


material_choices = (
    ("Silk"), ("Velvet"), ("Satin"),
)

color_choices = (
    ("Red"), ("Green"), ("Blue"),
)


class Product(models.Model):
    """Model for Product"""
    name = models.CharField(max_length=50)
    material = models.CharField(choices=material_choices, default="Silk")
    color = models.CharField(choices=color_choices, default="Red")
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
