from django.db import models


class NewsLetter(models.Model):
    email = models.EmailField()

    class Meta:
        app_label = 'car_showroom'
        verbose_name = 'News Letter'
        verbose_name_plural = 'News Letters'

    def __str__(self):
        return f'News letter for {self.email}'
