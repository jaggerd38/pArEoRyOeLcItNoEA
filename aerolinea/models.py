from django.db import models
from django.utils import timezone
from django.contrib import admin

class Avion(models.Model):
    nombre = models.CharField(max_length=30)
    modeloavion = models.CharField(max_length=30)
    capacidad = models.IntegerField()

    def __str__(self):
        respuesta = str(self.pk) + ' - ' +self.nombre
        return respuesta

class Pasajero(models.Model):
    nombre = models.CharField(max_length=200)
    edad = models.IntegerField()
    dpi = models.IntegerField(null=True)
    telefono = models.IntegerField()
    correo = models.EmailField()
    SEXO = (
		('M', 'Masculino'),
		('F','Femenino'))
    sexo = models.CharField(max_length=1,choices=SEXO)

    def __str__(self):
        respuesta = self.nombre + ' - ' + str(self.dpi)
        return respuesta

class Vuelo(models.Model):
    aerolinea = models.CharField(max_length=50)
    hora = models.DateTimeField()
    origen = models.CharField(max_length=200)
    destino = models.CharField(max_length=200)
    pasajeros = models.ManyToManyField(Pasajero, through='Viajar')
    avion = models.ForeignKey(Avion, null=True)

    def __str__(self):
        respuesta = str(self.pk) + ' - ' + self.destino
        return respuesta

class Viajar(models.Model):
    pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE)
    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)

class ViajarInLine(admin.TabularInline):
    model = Viajar
    extra = 1

class PasajeroAdmin(admin.ModelAdmin):
    inlines = (ViajarInLine,)

class VueloAdmin (admin.ModelAdmin):
    inlines = (ViajarInLine,)

class Boleto(models.Model):
    CLASEVUELO = (
		('T','Turista'),
		('E','Ejecutivo'),
		)
    clase = models.CharField(max_length=1,choices=CLASEVUELO)
    costo = models.PositiveIntegerField()
    numeroasiento = models.CharField(max_length=50)
    pasajero = models.ForeignKey(Pasajero)
    vuelo = models.ForeignKey(Vuelo)

    def __str__(self):
        respuesta = str(self.pk) + ' - ' +self.pasajero.nombre
        return respuesta
