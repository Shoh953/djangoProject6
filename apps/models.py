from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    descriptions = models.TextField
    price = models.DecimalField
    image = models.ImageField(upload_to='product/')
    file = models.FileField(upload_to='')
    data_added = models.DateField(auto_now_add=True)


class Blog(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
