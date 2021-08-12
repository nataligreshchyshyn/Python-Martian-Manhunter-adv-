"""car_dealer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from car_showroom import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', views.CarListView.as_view(), name='cars'),
    path('cars/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('dealers/', views.DealerListView.as_view(), name='dealers'),
    path('dealers/<int:pk>/', views.DealerDetailView.as_view(), name='dealer_detail'),
    path('api/cars/', views.car_serialize_list, name='api_cars'),
    path('api/cars/<int:pk>/', views.car_serialize_detail, name='api_car_detail'),
]
