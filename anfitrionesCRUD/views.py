from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Anfitrion
from .forms import AnfitrionForm

def lista_anfitriones(request):
    anfitriones = Anfitrion.objects.all()
    return render(request, 'anfitriones/lista_anfitriones.html', {'anfitriones': anfitriones})

def agregar_anfitrion(request):
    if request.method == 'POST':
        form = AnfitrionForm(request.POST)
        if form.is_valid():
            form.save()
            # notificacion
            messages.success(request, 'Anfitrión agregado exitosamente.')
            return redirect('/')

    else:
        form = AnfitrionForm()
    return render(request, 'anfitriones/agregar.html', {'form': form})

def modificar_anfitrion(request, anfitrion_id):
    anfitrion = get_object_or_404(Anfitrion, idAnfitrion=anfitrion_id)

    if request.method == 'POST':
        form = AnfitrionForm(request.POST, instance=anfitrion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Información del anfitrión actualizada.')
            return redirect('/')
    else:
        form = AnfitrionForm(instance=anfitrion)

    return render(request, 'anfitriones/modificar.html', {'form': form, 'anfitrion': anfitrion})

def eliminar_anfitrion(request, anfitrion_id):
    anfitrion = get_object_or_404(Anfitrion, idAnfitrion=anfitrion_id)
    anfitrion.delete()
    messages.success(request, 'Anfitrión eliminado.')
    return redirect('anfitrionesCRUD:lista_anfitriones')