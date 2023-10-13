from django.db import models
from django.utils.timezone import now


# Create your models here.

class CarMake(models.Model):
    name=models.CharField(max_length=30)
    desc=models.CharField(max_length=250)
    brand=models.CharField(max_length=20)
    def __str__(self):
        print('Name is {self.name} \n Description is {self.desc} \n Brand is {self.brand}')

class CarModel(models.Model):
     carmake = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
     dealer_id = models.IntegerField()
     name = models.CharField(max_length=30)
     car_type = models.CharField(max_length=10,choices=(('SEDAN','Sedan'),('SUV','SUV'),('WAGON','Wagon')))
     year = models.DateField(null=True)
     color = models.CharField(max_length=10)
     def __str__(self):
         print('Dealer ID is {self.dealer_id} \n Name is {self.name} \n Type is {self.car_type} \n Year is {self.year} \n Color is {self.color}')
     
# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data

