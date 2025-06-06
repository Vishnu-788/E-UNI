from django.db import models

class Order(models.Model):
    class PaymentStatus(models.TextChoices):
        PENDING = 'pending', 'Pending'
        SUCCESSFUL = 'successful', 'Successful'  # fix spelling 🙃
        FAILED = 'failed', 'Failed'

    class DeliveryStatus(models.TextChoices):
        PROCESSING = 'processing', 'Processing'
        SHIPPED = 'shipped', 'Shipped'
        DELIVERED = 'delivered', 'Delivered'
        CANCELLED = 'cancelled', 'Cancelled'

    product            = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    shop               = models.ForeignKey('shop.Shop', on_delete=models.CASCADE)
    user               = models.ForeignKey('users.User', on_delete=models.CASCADE)
    quantity           = models.PositiveIntegerField(default=1)
    ordered_date       = models.DateTimeField(auto_now_add=True)
    payment_status     = models.CharField(
                            max_length=15, 
                            choices=PaymentStatus.choices, 
                            null=False,
                            blank=False,
                            default=PaymentStatus.PENDING
                        )
    delivery_status    = models.CharField(
                            max_length=15, 
                            choices=DeliveryStatus.choices, 
                            null=False, 
                            blank=False, 
                            default=DeliveryStatus.PROCESSING
                        )
    total_price        = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_phone     = models.CharField(max_length=15)
    shipping_address   = models.TextField(null=False, blank=False)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"
    
    @property
    def get_total_price(self):
        return self.product.price * self.quantity
    
    def save(self, *args, **kwargs):
        self.total_price = self.get_total_price
        super().save(*args, **kwargs)