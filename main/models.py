from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    

    @property
    def __str__(self):
        return f"name : {self.name}, price : {self.price}"
