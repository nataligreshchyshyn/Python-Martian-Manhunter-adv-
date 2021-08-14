from django.urls import path

from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.CarListView.as_view(), name='cars_list'),
    path('<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
    path('api/cars/', views.car_serialize_list, name='api_cars'),
    path('api/cars/<int:pk>/', views.car_serialize_detail, name='api_car_detail'),
]
