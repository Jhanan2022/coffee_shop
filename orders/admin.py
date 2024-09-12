from django.contrib import admin
from orders.models import Order, OrderProduct

class OrderProductInlineAdmin(admin.TabularInline):
    model = OrderProduct
    extra  = 0

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ["user", "order_date", "is_active"]
    search_fields = ["user"]
    inlines = [OrderProductInlineAdmin]

admin.site.register(Order, OrderAdmin)