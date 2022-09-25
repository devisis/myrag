import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product


class Order(models.Model):
    order_number = models.CharField(max_length=40, null=False, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=120, null=False, blank=False)
    email = models.EmailField(max_length=320, null=False, blank=False)
    street_1 = models.CharField(max_length=150, null=False, blank=False)
    street_2 = models.CharField(max_length=150, null=True, blank=True)
    county = models.CharField(max_length=80, null=False, blank=False)
    postcode = models.CharField(max_length=15, null=False, blank=False)
    total = models.DecimalField(
        max_digits=10, default=0, decimal_places=2, null=False)

    def __str__(self):
        return self.order_number

    def _generate_order_number(self):
        """
        Generate number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        update total each time a new item is added
        """
        self.total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        """
        set order number if it doesnt already exist
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, null=False, blank=False, 
        related_name='lineitems')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.IntegerField(default=0, null=False, blank=False)
    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False)

    def save(self, *args, **kwargs):
        """
        Update the total of the order line item
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)
