from django import forms

from .models import Avion, Pasajero, Vuelo, Boleto

class AvionForm(forms.ModelForm):
    class Meta:
        model = Avion
        fields = ('nombre', 'modeloavion', 'capacidad')

class PasajeroForm(forms.ModelForm):
    class Meta:
        model = Pasajero
        fields = ('nombre', 'edad', 'dpi', 'telefono', 'correo', 'sexo')

class VueloForm(forms.ModelForm):
    class Meta:
        model = Vuelo
        fields = ('aerolinea', 'hora', 'origen', 'destino', 'pasajeros', 'avion')

    def __init__ (self, *args, **kwargs):

        super(VueloForm, self).__init__(*args, **kwargs)

        self.fields["pasajeros"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["pasajeros"].queryset = Pasajero.objects.all()
        self.fields["pasajeros"].help_text = "SELECCIONE LOS PASAJEROS DEL VUELO"

class BoletoForm(forms.ModelForm):
    class Meta:
        model = Boleto
        fields = ('clase', 'costo', 'numeroasiento', 'pasajero', 'vuelo')
