from .models import Order
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class OrderListView(ListView):
    template_name = 'orders/list.html'
    context_object_name = 'orders'
    paginate_by = 20

    def get_queryset(self):
        return Order.objects.all()


class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/detail.html'
