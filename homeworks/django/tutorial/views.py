from random import randint
from django.shortcuts import render


def status(request):
    context = {
        "color": (lambda: "%06x" % randint(0, 0xffffff))(),
    }
    return render(request, "tutorial/status.html", context)
