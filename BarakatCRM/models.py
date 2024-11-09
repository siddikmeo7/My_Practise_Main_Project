from django.db import models
from django.core.validators import RegexValidator


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__ (self):
        return self.name

class Colour(models.Model):
    name = models.CharField(max_length=50)

    def __str__ (self):
        return self.name
    
class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__ (self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__ (self):
        return self.name
    
class Region(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City,on_delete=models.CASCADE)

    def __str__ (self):
        return self.name
    
class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254,null=True)
    phone_number = models.CharField(max_length=15,validators=[RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be in the format: '+999999999'. Up to 15 digits allowed."),

        ],
        help_text="Enter phone number in international format, e.g., +123456789012345"
    )
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return f"{self.first_name} {self.last_name}"
    
class Product(models.Model):
    category =  models.ForeignKey(Category,on_delete=models.CASCADE)
    index = models.CharField(max_length=50,null=True)
    colour = models.ForeignKey(Colour,on_delete=models.CASCADE)
    price =  models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    up_to =  models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    sold =  models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField()
    sold_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return f"{self.category}"
    
class Sklad(models.Model):
    name = models.CharField(max_length=50)

    def __str__ (self):
        return self.name

class SkladProducts(models.Model):
    sklad = models.ForeignKey(Sklad,on_delete=models.CASCADE)
    shoes = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__ (self):
        return f"{self.sklad} - {self.shoes}"