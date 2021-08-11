from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Order(models.Model):
    car = models.ForeignKey(
        'car_showroom.Car',
        on_delete=models.CASCADE,
        related_name='orders',
    )

    STATUS_RECEIVED = 'received'
    STATUS_WAITING = 'waiting'
    STATUS_ACTIVE = 'active'
    STATUS_CLOSED = 'closed'

    STATUS_CHOICES = (
        (STATUS_RECEIVED, 'Received'),
        (STATUS_WAITING, 'Waiting'),
        (STATUS_ACTIVE, 'In progress'),
        (STATUS_CLOSED, 'Closed'),
    )

    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default=STATUS_WAITING,
        blank=True
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = PhoneNumberField()
    message = models.TextField()

    class Meta:
        app_label = 'car_showroom'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'Order from {self.first_name} {self.last_name}'
