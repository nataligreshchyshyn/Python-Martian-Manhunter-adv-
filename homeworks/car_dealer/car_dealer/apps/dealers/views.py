from .models import Dealer
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class DealerListView(ListView):
    template_name = 'dealers/list.html'
    context_object_name = 'dealers'
    paginate_by = 20

    def get_queryset(self):
        return Dealer.objects.all()


class DealerDetailView(DetailView):
    model = Dealer
    template_name = 'dealers/detail.html'
