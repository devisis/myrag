from django.db import models


class Product(models.Model):
    """Model for Product"""
    id = models.AutoField()
    name = models.CharField(max_length=)
    material = models.Field.choices()
    color = models.CharField()
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    image = models.ImageField()

    def __str__(self):

class Review(models.Model):
    """Model for Reviews"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=200, blank=True)
    when_created = models.DateTimeField()