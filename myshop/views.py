from myshopapp.models import Product 
from django.views.generic.list import ListView


def products(request):
    """
    Render all the products
    """
    context = {
        'products': Product.objects.all()
    }
    return render(request, "products.html", context)


class HomeView(ListView):
    model = Product
    paginate_by = 10
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context
