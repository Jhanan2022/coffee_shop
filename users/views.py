from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class RegisterView(CreateView):
    form_class = UserCreationForm  # Formulario de registro estándar
    template_name = 'users/register.html'  # Template de registro personalizado
    success_url = reverse_lazy('login')  # Redirige a la página de login después del registro