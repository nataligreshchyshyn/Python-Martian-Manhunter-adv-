from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

from .models import Car
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# def car_list(request):
#     cars = Car.objects.all()
#     context = {'cars': cars}
#     return render(
#         request,
#         'cars/list.html',
#         context
#     )


class CarListView(ListView):
    template_name = 'cars/list.html'
    context_object_name = 'cars'
    paginate_by = 20

    def get_queryset(self):
        return Car.objects.all()


class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/detail.html'


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
