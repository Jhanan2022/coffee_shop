from django.urls import path
from .views import MyOrderView, add_product_to_order

urlpatterns = [
    path('mi-orden/', MyOrderView.as_view(), name="my_order"),
    path("agregar-producto/", add_product_to_order, name="add_product")
]