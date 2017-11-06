from django.contrib import admin
from aerolinea.models import Avion, Pasajero, PasajeroAdmin, Vuelo, VueloAdmin, Boleto, Viajar

admin.site.register(Avion)
admin.site.register(Boleto)
admin.site.register(Viajar)
admin.site.register(Vuelo, VueloAdmin)
admin.site.register(Pasajero, PasajeroAdmin)
admin.autodiscover()
