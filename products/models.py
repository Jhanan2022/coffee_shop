from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="nombre")
    description = models.TextField(max_length=500, verbose_name="descripcion")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="precio")
    available = models.BooleanField(default=True, verbose_name="disponible")
    photo = models.ImageField(
        upload_to="logos", null=True, blank=True, verbose_name="foto"
    )
    creation_date = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name="fecha de creacion"
    )

    def __str__(self) -> str:
        return self.name
