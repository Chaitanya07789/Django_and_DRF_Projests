from django.db import models
from utils.models import BaseModel
from accounts.models import Shopkeeper

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

    def __str__(self):
        return self.item_name
    
    def getFirstImage(self):
        if self.product_image.first():
            return self.product_image.first().image # reverse relation (reverse orm)
        
        return "https://static.vecteezy.com/system/resources/thumbnails/022/014/063/small/missing-picture-page-for-website-design-or-mobile-app-design-no-image-available-icon-vector.jpg"
    

class VarientOptions(BaseModel):
    varient_name = models.CharField(max_length=100)
    option_name = models.CharField(max_length=100)

    def __str__(self):
        return self.option_name


class ProductVarient(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_varient")
    varient_options = models.ManyToManyField(VarientOptions)

    def __str__(self):
        return f"Varient for {self.product.item_name}"

class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_image")

class VendorProducts(BaseModel):
    shopkeeper = models.ForeignKey(Shopkeeper, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    vender_selling_price = models.FloatField()
    dealer_price = models.FloatField()
    is_active = models.BooleanField(default=True)
    delivery_fee = models.FloatField(default=True)

    def get_product_details(self):
        return {
            "product_name": self.product.item_name,
            "image": self.product.getFirstImage()
        }