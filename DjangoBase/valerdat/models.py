from django.db import models

class Product(models.Model):

    reference = models.SlugField()
    name = models.CharField(max_length=255)
    volume = models.DecimalField(decimal_places=2, max_digits=14)
    created = models.DateTimeField()