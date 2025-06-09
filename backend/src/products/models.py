from django.db import models

# Create your models here.
class Product(models.Model):
    shop = models.ForeignKey('shop.Shop', on_delete=models.CASCADE, related_name='products')
    product = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, default="Description Not available")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    product_image = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.product

    def get_price(self):
        return self.price
