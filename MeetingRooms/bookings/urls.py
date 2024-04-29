
from django.urls import path

from .views import (
    home_view,
    SalaListView,
    SalaDetailView,
    SalaDeleteView,
    SalaUpdateView,
    SalaCreateView,
    user_login_view,
    user_logout_view,
    UserUpdateView,
    sala_search_view,
    ReservaListView,
    ReservaCreateView,
    ReservaDeleteView,
    ReservaDetailView,
    ReservaUpdateView,
    AccesorioListView,
    AccesorioCreateView,
    AccesorioDetailView,
    AccesorioDeleteView,
    AccesorioUpdateView,
   
    )

urlpatterns = [
    path("", home_view, name= 'home'),
    path("sala/list/", SalaListView.as_view(), name="sala-list"),
    path("sala/create/", SalaCreateView.as_view(),name= "sala-create"),
    path("sala/<int:pk>/detail/", SalaDetailView.as_view(), name= "sala-detail"),
    path("sala/<int:pk>/delete/", SalaDeleteView.as_view(), name= "sala-delete"),
    path("sala/<int:pk>/update/", SalaUpdateView.as_view(), name= "sala-update"),
    path("sala/buscar/", sala_search_view, name= 'sala-buscar'),
    path("login/", user_login_view, name="login"),
    path("logout/", user_logout_view, name="logout"),
    path("editar-perfil/", UserUpdateView.as_view(), name= 'editar-perfil'),
    path("reserva/list/", ReservaListView.as_view(), name= "reserva-list"),
    path("reserva/create/", ReservaCreateView.as_view(), name= "reserva-create"),
    path("reserva/<int:pk>/delete/", ReservaDeleteView.as_view(), name= 'reserva-delete'),
    path("reserva/<int:pk>/detail/", ReservaDetailView.as_view(),name= 'reserva-detail'),
    path("reserva/<int:pk>/update/", ReservaUpdateView.as_view(), name= "reserva-update"),
    path("accesorio/list/", AccesorioListView.as_view(), name= 'accesorio-list'),
    path("accesorio/create/", AccesorioCreateView.as_view(),name= "accesorio-create"),
    path("accesorio/<int:pk>/detail/", AccesorioDetailView.as_view(), name= "accesorio-detail"),
    path("accesorio/<int:pk>/delete/", AccesorioDeleteView.as_view(), name= "accesorio-delete"),
    path("accesorio/<int:pk>/update/", AccesorioUpdateView.as_view(), name= "accesorio-update")
]
