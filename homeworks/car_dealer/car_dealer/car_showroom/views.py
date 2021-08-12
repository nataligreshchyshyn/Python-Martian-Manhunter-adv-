from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

from car_showroom.models import Car, Order, Dealer
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# def car_list(request):
#     cars = Car.objects.all()
#     context = {'cars': cars}
#     return render(
#         request,
#         'car_showroom/cars/list.html',
#         context
#     )


class CarListView(ListView):
    template_name = 'car_showroom/cars/list.html'
    context_object_name = 'cars'
    paginate_by = 20

    def get_queryset(self):
        return Car.objects.all()


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_showroom/cars/detail.html'


class OrderListView(ListView):
    template_name = 'car_showroom/orders/list.html'
    context_object_name = 'orders'
    paginate_by = 20

    def get_queryset(self):
        return Order.objects.all()


class OrderDetailView(DetailView):
    model = Order
    template_name = 'car_showroom/orders/detail.html'


class DealerListView(ListView):
    template_name = 'car_showroom/dealers/list.html'
    context_object_name = 'dealers'
    paginate_by = 20

    def get_queryset(self):
        return Dealer.objects.all()


class DealerDetailView(DetailView):
    model = Dealer
    template_name = 'car_showroom/dealers/detail.html'


def car_serialize_list(request):
    obj = Car.objects.all()
    data = serializers.serialize('json', obj)
    # return JsonResponse(data=data, safe=False)
    return HttpResponse(
        data,
        content_type='application/json'
    )  # decided to keep HttpResponse because of nicely formatted JSON response


def car_serialize_detail(request, pk):
    obj = Car.objects.get(pk=pk)
    data = serializers.serialize('json', [obj, ])
    return HttpResponse(
        data,
        content_type='application/json'
    )
