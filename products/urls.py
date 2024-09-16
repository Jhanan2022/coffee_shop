from django.urls import path
from products.views import ProductFormView, ProductListAPI, ProductListView

urlpatterns = [
    path("agregar/", ProductFormView.as_view(), name="add_product"),
    path("api/", ProductListAPI.as_view(), name="list_product_api"),
    path("", ProductListView.as_view(), name="list_product"),
]
