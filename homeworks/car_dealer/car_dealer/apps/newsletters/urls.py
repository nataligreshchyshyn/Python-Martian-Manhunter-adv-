from django.urls import path
from .views import NewsLetterModelView, SuccessView

app_name = 'newsletters'


urlpatterns = [
    path('subscribe/', NewsLetterModelView.as_view(), name='email-page'),
    path('success/', SuccessView.as_view(), name='success'),
]
