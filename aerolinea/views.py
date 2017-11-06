from django.shortcuts import render, render, get_object_or_404, redirect
from django.contrib import messages
from .forms import AvionForm, PasajeroForm, VueloForm, BoletoForm
from aerolinea.models import Avion, Pasajero, Vuelo, Viajar, Boleto
from django.contrib.auth.decorators import login_required


@login_required
def main_index(request):
    return render(request, 'aerolinea/main.html')


##############################    VUELOS     ###########################################################################################

@login_required
def vuelo_index(request):
    vuelo = Vuelo.objects.order_by('pk').reverse()
    return render(request, 'aerolinea/vuelo_index.html', {'p':vuelo})

@login_required
def detalle_vuelo(request, pk):
    vuelo = get_object_or_404(Vuelo, pk=pk)
    return render(request, 'aerolinea/detalle_vuelo.html', {'p': vuelo})

@login_required
def vuelo_nuevo(request):
    if request.method == "POST":
        formulario = VueloForm(request.POST)
        if formulario.is_valid():
            vuelo = Vuelo.objects.create(aerolinea=formulario.cleaned_data['aerolinea'],
                    numero = formulario.cleaned_data['numero'], hora = formulario.cleaned_data['hora'],
                    origen = formulario.cleaned_data['origen'], destino = formulario.cleaned_data['destino'],
                    avion = formulario.cleaned_data['avion'])
            for pasajero_id in request.POST.getlist('pasajeros'):
                viajar = Viajar(pasajero_id=pasajero_id, vuelo_id = vuelo.id)
                viajar.save()
            return redirect('ver_vuelo', pk=vuelo.pk)
    else:
        formulario = VueloForm()
    return render(request, 'aerolinea/vuelo_editar.html', {'formulario': formulario})

@login_required
def vuelo_editar(request, pk):
    vuelo = get_object_or_404(Vuelo, pk=pk)
    if request.method == "POST":
        formulario = VueloForm(request.POST, instance=vuelo)
        if formulario.is_valid():
            vuelo = Vuelo.objects.create(aerolinea=formulario.cleaned_data['aerolinea'],
                    numero = formulario.cleaned_data['numero'], hora = formulario.cleaned_data['hora'],
                    origen = formulario.cleaned_data['origen'], destino = formulario.cleaned_data['destino'],
                    avion = formulario.cleaned_data['avion'])
            for pasajero_id in request.POST.getlist('pasajeros'):
                viajar = Viajar(pasajero_id=pasajero_id, vuelo_id = vuelo.id)
                viajar.save()
            return redirect('ver_vuelo', pk=vuelo.pk)
    else:
        formulario = VueloForm(instance=vuelo)
    return render(request, 'aerolinea/vuelo_editar.html', {'formulario': formulario})

@login_required
###############################     AVIONES      ##########################################################################################

@login_required
def avion_index(request):
    avion = Avion.objects.order_by('pk').reverse()
    return render(request, 'aerolinea/avion_index.html', {'p':avion})

@login_required
def detalle_avion(request, pk):
    avion = get_object_or_404(Avion, pk=pk)
    return render(request, 'aerolinea/detalle_avion.html', {'p': avion})

@login_required
def avion_nuevo(request):
    if request.method == "POST":
        formulario = AvionForm(request.POST)
        if formulario.is_valid():
            avion = formulario.save(commit=False)
            avion.save()
            return redirect('ver_avion', pk=avion.pk)
    else:
        formulario = AvionForm()
    return render(request, 'aerolinea/avion_editar.html', {'formulario': formulario})

@login_required
def avion_editar(request, pk):
    avion = get_object_or_404(Avion, pk=pk)
    if request.method == "POST":
        formulario = AvionForm(request.POST, instance=avion)
        if formulario.is_valid():
            avion = formulario.save(commit=False)
            avion.autor = request.user
            avion.save()
            return redirect('ver_avion', pk=avion.pk)
    else:
        formulario = AvionForm(instance=avion)
    return render(request, 'aerolinea/avion_editar.html', {'formulario': formulario})


##############################    PASAJEROS     ###########################################################################################

@login_required
def pasajero_index(request):
    pasajero = Pasajero.objects.order_by('pk').reverse()
    return render(request, 'aerolinea/pasajero_index.html', {'p':pasajero})

@login_required
def detalle_pasajero(request, pk):
    pasajero = get_object_or_404(Pasajero, pk=pk)
    return render(request, 'aerolinea/detalle_pasajero.html', {'p': pasajero})

@login_required
def pasajero_nuevo(request):
    if request.method == "POST":
        formulario = PasajeroForm(request.POST)
        if formulario.is_valid():
            pasajero = formulario.save(commit=False)
            pasajero.save()
            return redirect('ver_pasajero', pk=pasajero.pk)
    else:
        formulario = PasajeroForm()
    return render(request, 'aerolinea/pasajero_editar.html', {'formulario': formulario})

@login_required
def pasajero_editar(request, pk):
    pasajero = get_object_or_404(Pasajero, pk=pk)
    if request.method == "POST":
        formulario = PasajeroForm(request.POST, instance=pasajero)
        if formulario.is_valid():
            pasajero = formulario.save(commit=False)
            pasajero.autor = request.user
            pasajero.save()
            return redirect('ver_pasajero', pk=pasajero.pk)
    else:
        formulario = PasajeroForm(instance=pasajero)
    return render(request, 'aerolinea/pasajero_editar.html', {'formulario': formulario})

##############################    BOLETOS     ###########################################################################################

@login_required
def boleto_index(request):
    boleto = Boleto.objects.order_by('pk').reverse()
    return render(request, 'aerolinea/boleto_index.html', {'p':boleto})

@login_required
def detalle_boleto(request, pk):
    boleto = get_object_or_404(Boleto, pk=pk)
    return render(request, 'aerolinea/detalle_boleto.html', {'p': boleto})

def boleto_nuevo(request):
    if request.method == "POST":
        formulario = BoletoForm(request.POST)
        if formulario.is_valid():
            boleto = formulario.save(commit=False)
            boleto.save()
            return redirect('ver_boleto', pk=boleto.pk)
    else:
        formulario = BoletoForm()
    return render(request, 'aerolinea/boleto_editar.html', {'formulario': formulario})

@login_required
def boleto_editar(request, pk):
    boleto = get_object_or_404(Boleto, pk=pk)
    if request.method == "POST":
        formulario = BoletoForm(request.POST, instance=boleto)
        if formulario.is_valid():
            boleto = formulario.save(commit=False)
            boleto.autor = request.user
            boleto.save()
            return redirect('ver_boleto', pk=boleto.pk)
    else:
        formulario = BoletoForm(instance=boleto)
    return render(request, 'aerolinea/boleto_editar.html', {'formulario': formulario})
