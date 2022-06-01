from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    image=models.FileField(default='default.jpg')
    def __str__(self):
        return f'category:{self.name}'

    def get_absolute_url(self):
        return reverse('categorypage')

class Product(models.Model):
    name=models.CharField(max_length=1000,unique=True)
    desc=models.TextField(max_length=10000)
    price=models.DecimalField(max_digits=9,decimal_places=2)
    image=models.FileField(default='default.jpg')
    catid=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('categorypage')
    

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)  
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
            return str(self.id)  

class Bill(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)  
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now=True)

    def __str__(self):
            return str(self.id)

class UserBill(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    products=models.CharField(max_length=10000) 
    quantity=models.PositiveIntegerField(default=1)
    total_anount=models.DecimalField(max_digits=9,decimal_places=2)
    discounted_amount=models.DecimalField(max_digits=9,decimal_places=2)
    discout=models.DecimalField(max_digits=9,decimal_places=2)
    ordered_date=models.DateTimeField(auto_now=True)

    def __str__(self):
            return str(self.id)