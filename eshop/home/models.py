from django.db import models
from django.contrib.auth.models import User


# product information table.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='' , null=True , blank=True)
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return self.name


#card information table
class UserCard(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, blank=True)


    def __str__(self):
        return self.user_id.username