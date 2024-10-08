from django.db import models
from django.contrib.auth.models import User

from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True, max_length=20)

    def __str__(self):
        return f"Order {self.id} by {self.user}"


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(
        default=1
    )  # Asegúrate de que `default` esté definido

    def __str__(self):
        return f"Order {self.order.id} - Product {self.product.id}"
