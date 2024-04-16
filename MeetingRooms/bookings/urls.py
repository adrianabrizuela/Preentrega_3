
from django.urls import path

from django.http import HttpResponse


def mi_vista(xx):
    return HttpResponse("<h3>Bienvenidos a mi reserva</h3>")

urlpatterns = [
    path("",mi_vista),
]
