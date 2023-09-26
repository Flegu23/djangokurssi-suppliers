from django.db import models

class Supplier(models.Model):
    companyname = models.CharField(max_length= 50, default="firma")
    contactname = models.CharField(max_length= 50, default="firma")
    address = models.CharField(max_length= 100, default="firma")
    phone = models.CharField(max_length= 20, default="firma")
    email = models.CharField(max_length= 50, default="firma")
    country = models.CharField(max_length= 50, default="firma")

    def __str__(self):
        return f"{self.companyname} from {self.country}"


class Product(models.Model):
    companyname = models.CharField(max_length= 50, default="firma")
    productname = models.CharField(max_length= 20, default="laku")
    packagesize = models.CharField(max_length= 20, default = 3)
    unitprice = models.DecimalField(max_digits=8, decimal_places=2, default=1.00)
    unitsinstock = models.IntegerField(default="laku")
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.productname} produced by {self.companyname}"
    
class Car(models.Model):
    companyname = models.CharField(max_length= 50, default="firma")
    carname = models.CharField(max_length= 50, default="firma")
    carmodel = models.CharField(max_length= 50, default="firma")
    drivenkm = models.DecimalField(max_digits=8, decimal_places=2, default=1.00)

    def __str__(self):
        return f"{self.carmodel} owned by {self.companyname}"
    
class Shop(models.Model):
    companyname = models.CharField(max_length= 50, default="firma")
    shoptown = models.CharField(max_length= 50, default="firma")
    shopaddress = models.CharField(max_length= 50, default="firma")

    def __str__(self):
        return f"{self.shoptown} owned by {self.companyname}"