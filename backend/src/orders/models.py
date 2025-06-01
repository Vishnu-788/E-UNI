from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Order(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('successfull', 'Successfull'),
        ('failed', 'Failed')
    ]

    DELIVERY_STATUS_CHOICES = [
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled')
    ]

    product_id         = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='orders')
    user_id            = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    quantity           = models.PositiveIntegerField(default=1)
    ordered_date       = models.DateTimeField(auto_now_add=True)
    payment_status     = models.CharField(max_length=15, choices=PAYMENT_STATUS_CHOICES, null=False, blank=False)
    delivery_status    = models.CharField(max_length=15, choices=DELIVERY_STATUS_CHOICES, null=False, blank=False)
    total_price        = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_phone     = models.CharField(max_length=15)
    shipping_address   = models.TextField(null=False, blank=False)

    def __str__(self):
        return f"Order #{self.id} - {self.user_id.username}"
    
    @property
    def get_total_price(self):
        return self.product_id.price * self.quantity
    
    def save(self, *args, **kwargs):
        self.total_price = self.get_total_price
        super().save(*args, **kwargs)