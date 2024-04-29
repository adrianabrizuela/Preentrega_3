from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Sala(models.Model):
    class Tipo(models.TextChoices):
        AUDITORIO = 'AUD', 'Auditorio'
        SALA_DE_CONFERENCIAS = 'CON', 'Sala de Conferencias'
        AULA = 'AUL', 'Aula'
        LABORATORIO = 'LAB', 'Laboratorio'

    nombre = models.CharField(max_length=40)
    capacidad = models.IntegerField()
    disponible = models.BooleanField(default=True)  # Puedes definir un valor predeterminado si lo deseas
    tipo = models.CharField(
        max_length=3,
        choices=Tipo.choices,
        default=Tipo.AULA,
    )

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"


class Accesorio(models.Model):
    class Tipo(models.TextChoices):
        CAFETERA = 'Cafetera', 'Cafetera'
        PROYECTOR = 'Proyector', 'Proyector'
        MICROFONO = 'Micrófono', 'Micrófono'
        PIZARRA = 'Pizarra', 'Pizarra'
    
    nombre_usuario = models.ForeignKey(User, null= True, on_delete= models.SET_NULL)
    nombre = models.CharField(
        max_length=15,  # Ajusta la longitud máxima según tus necesidades
        choices=Tipo.choices,
        default=Tipo.PIZARRA,
    )
    descripcion = models.TextField(blank=True, null=True)
   
    def __str__(self):
        return self.get_nombre_display()



class Reserva(models.Model):
    nombre_de_usuario = models.ForeignKey(User, null= True, on_delete= models.SET_NULL)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now)
    hora_inicio = models.TimeField(default=timezone.now)
    hora_fin = models.TimeField(default=timezone.now)
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre_de_usuario} - {self.sala.nombre} - {self.fecha}"
    

