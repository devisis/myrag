from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    description = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.email
