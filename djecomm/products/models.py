from django.db import models
from utils.models import BaseModel

class Category(BaseModel):
    name = models.CharField(max_length=100)
    comission_percentage = models.IntegerField(default=10)

    def __str__(self):
        return self.name
    
class Subcategory(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="sub_categories")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class BrandName(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product_category")
    subcategories = models.ForeignKey(Subcategory, on_delete= models.CASCADE, related_name="product_sub_category")
    brand = models.ForeignKey(BrandName, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_sku = models.CharField(max_length=100 , unique=True)
    hsn_code = models.CharField(max_length=100)
    maximum_retail_price = models.FloatField()
    parent_product = models.ForeignKey("Product", related_name="variant_name", on_delete=models.CASCADE, null=True, blank=True)
