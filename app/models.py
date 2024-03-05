from django.db import models

# Create your models here.

class ProductCatagory(models.Model):
    product_catagory_id=models.IntegerField(primary_key=True)
    product_catagory_name=models.CharField(max_length=100)

    def _str_(self):
        return self. product_catagory_name
    
class Product(models.Model):
    product_catagory_id=models.ForeignKey(ProductCatagory,on_delete=models.CASCADE)
    product_id=models.IntegerField()
    product_name=models.CharField(max_length=100)
    product_price=models.IntegerField()
    product_brand=models.CharField(max_length=100)

    def _str_(self):
        return self.product_name