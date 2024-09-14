from django.shortcuts import redirect, render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order
from .forms import OrderProductForm
from django.contrib.auth.decorators import login_required


class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = "order"

    def get_object(self, queryset=None):
        order = Order.objects.filter(
            is_active=True, user=self.request.user
        ).first()  # Obtenemos la primera orden activa del usuario
        return order

    def get_context_data(self, **kwargs):
        # Llamamos al contexto original
        context = super().get_context_data(**kwargs)

        # Calculamos el subtotal
        order = self.get_object()
        if order is None:
            context["subtotal"] = 0
        else:
            context["subtotal"] = sum(
                [
                    item.product.price * item.quantity
                    for item in order.orderproduct_set.all()
                ]
            )

        return context


@login_required
def add_product_to_order(request):
    if request.method == 'POST':
        form = OrderProductForm(request.POST)
        if form.is_valid():
            # Obtener o crear la orden activa del usuario
            order, _ = Order.objects.get_or_create(
                is_active=True,
                user=request.user
            )
           
            # Obtener el producto del formulario
            product = form.cleaned_data['product']
            
            # Intentar obtener el OrderProduct existente para la combinación de producto y orden
            order_product, created = order.orderproduct_set.get_or_create(
                product=product
            )
            
            if created:
                # Si se creó un nuevo OrderProduct, establecer la cantidad en 1
                order_product.quantity = 1
            else:
                # Si ya existe, incrementar la cantidad
                order_product.quantity += 1
            
            # Guardar el OrderProduct
            order_product.save()
            
            return redirect('my_order')
    else:
        form = OrderProductForm()
    
    return render(request, 'orders/create_order_product.html', {'form': form})