from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Reserva, Sala, Accesorio
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import SalaSearchForm


def home_view(request):
    return render(request, "bookings/home.html")


#-----------------------------------------------------------------
#                      CRUD SALAS
#-----------------------------------------------------------------

# List

class SalaListView(LoginRequiredMixin, ListView):
    model = Sala
    template_name = "bookings/vbc/sala_list.html"
    context_object_name = "ADRIANDARGELOS"


class SalaDetailView(LoginRequiredMixin, DetailView):
    model = Sala
    template_name = "bookings/vbc/sala_detail.html"
    context_object_name = "GUSTAVOCERATI"


class SalaDeleteView(LoginRequiredMixin, DeleteView):
    model = Sala
    template_name = "bookings/vbc/sala_confirm_delete.html"
    success_url = reverse_lazy("sala-list")


class SalaUpdateView(LoginRequiredMixin, UpdateView):
    model = Sala
    template_name = "bookings/vbc/sala_form.html"
    fields = ["nombre", "disponible", "capacidad"]
    context_object_name = "sala"
    success_url = reverse_lazy("sala-list")


class SalaCreateView(LoginRequiredMixin, CreateView):
    model = Sala
    template_name = "bookings/vbc/sala_form.html"
    fields = ["nombre","tipo", "disponible", "capacidad"]
    success_url = reverse_lazy("sala-list")



def sala_search_view(request):
    if request.method == "GET":
        form = SalaSearchForm()
        return render(
            request, "bookings/form_search.html", context={"search_form": form}
        )
    elif request.method == "POST":
        #  devolverle a "chrome" la lista de reservas encontrada o avisar que no se encontró nada
        form = SalaSearchForm(request.POST)
        if form.is_valid():
            nombre_de_sala = form.cleaned_data["nombre"]
            salas_encontradas = Sala.objects.filter(nombre= nombre_de_sala).all()
            contexto_dict = {"ADRIANDARGELOS": salas_encontradas}
            return render(request, "bookings/vbc/sala_list.html", contexto_dict)
        else: 
            return render(
            request, "bookings/form_search.html", context={"search_form": form}
        )

#-----------------------------------------------------------------
#                      CRUD RESERVAS
#-----------------------------------------------------------------

class ReservaListView(LoginRequiredMixin, ListView):
    model = Reserva
    template_name = "bookings/vbc/reserva_list.html"
    context_object_name = "PETERPAN"


class ReservaDetailView(LoginRequiredMixin, DetailView):
    model = Reserva
    template_name = "bookings/vbc/reserva_detail.html"
    context_object_name = "CAMPANITA"


class ReservaDeleteView(LoginRequiredMixin, DeleteView):
    model = Reserva
    template_name = "bookings/vbc/reserva_confirm_delete.html"
    success_url = reverse_lazy("reserva-list")


class ReservaUpdateView(LoginRequiredMixin, UpdateView):
    model = Reserva
    template_name = "bookings/vbc/reserva_form.html"
    fields = ["nombre_de_usuario","sala","fecha", "hora_inicio", "hora_fin","descripcion"]
    context_object_name = "reserva"
    success_url = reverse_lazy("reserva-list")


class ReservaCreateView(LoginRequiredMixin, CreateView):
    model = Reserva
    template_name = "bookings/vbc/reserva_form.html"
    fields = ["nombre_de_usuario","sala","fecha", "hora_inicio", "hora_fin","descripcion"]
    success_url = reverse_lazy("reserva-list")


# def search_with_form_view(request):
#     from .forms import ReservaSearchForm
#     form = ReservaSearchForm()
#     return render (request, "bookings/usuario_form_search.html", context = {"usuario_search_form":form})
   
# def search_with_form_view(request):
#     if request.method == "GET":
#         form = ReservaSearchForm()
#         return render(
#             request, "bookings/usuario_form_search.html", context={"usuario_search_form": form}
#         )
#     elif request.method == "POST":
#         #  devolverle a "chrome" la lista de reservas encontrada o avisar que no se encontró nada
#         form = ReservaSearchForm(request.POST)
#         if form.is_valid():
#             nombre = form.cleaned_data["nombre_de_usuario"]
#             reservas_encontradas = Reserva.objects.filter(nombre= nombre).all()
#             contexto_dict = {"PETERPAN": reservas_encontradas}
#             return render(request, "bookings/vbc/reserva_list.html", contexto_dict)
#         else: 
#             return render(
#             request, "bookings/usuario_form_search.html", context={"usuario_search_form": form}
#         )


#-----------------------------------------------------------------
#                      CRUD ACCESORIOS
#-----------------------------------------------------------------

class AccesorioListView(LoginRequiredMixin, ListView):
    model = Accesorio
    template_name = "bookings/vbc/accesorio_list.html"
    context_object_name = "DONALD"


class AccesorioDetailView(LoginRequiredMixin, DetailView):
    model = Accesorio
    template_name = "bookings/vbc/accesorio_detail.html"
    context_object_name = "DAISY"


class AccesorioDeleteView(LoginRequiredMixin, DeleteView):
    model = Accesorio
    template_name = "bookings/vbc/accesorio_confirm_delete.html"
    success_url = reverse_lazy("reserva-list")


class AccesorioUpdateView(LoginRequiredMixin, UpdateView):
    model = Accesorio
    template_name = "bookings/vbc/accesorio_form.html"
    fields = ["nombre_usuario","nombre","descripcion"]
    context_object_name = "accesorio"
    success_url = reverse_lazy("accesorio-list")


class AccesorioCreateView(LoginRequiredMixin, CreateView):
    model = Accesorio
    template_name = "bookings/vbc/accesorio_form.html"
    fields = ["nombre_usuario","nombre","descripcion"]
    success_url = reverse_lazy("accesorio-list")




#-----------------------------------------------------------------
#                      login/logout
#-----------------------------------------------------------------


from django.contrib.auth import logout,login
from django.contrib.auth.forms import AuthenticationForm


def user_login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.user_cache
            if user is not None:
                login(request, user)
                return redirect("home")

    return render(request, "bookings/login.html", {"MICHAELSTIPE": form})

def user_logout_view(request):
    logout(request)
    return redirect("login")


#-----------------------------------------------------------------
#                      editar usuario
#-----------------------------------------------------------------

from django.contrib.auth.models import User
from .forms import UserEditForm

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'bookings/user_edit_form.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user