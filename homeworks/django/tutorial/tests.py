from http import HTTPStatus

from django.test import TestCase
from django.test import Client

from django.urls import reverse


class StatusViewTests(TestCase):
    client = Client()

    def test_status_view(self):
        response = self.client.get(reverse('status'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), "OK")
