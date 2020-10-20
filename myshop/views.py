from myshopapp.models import Product, Category 
from django.views.generic.list import ListView


class HomeView(ListView):
    model = Product
    paginate_by = 10
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = Category.objects.all()
 
        query = self.request.GET.get('q')
        category = self.request.GET.get('category')
        if query:
            context['products'] = self.model.objects.filter(name__icontains=query)
        elif category:
            context['products'] = self.model.objects.filter(category__name=category)

        else:
            context['products'] = self.model.objects.all()

        return context
