# views.py
from django.shortcuts import render, redirect
from .forms import VehicleForm
from .models import Vehicle
from .serial_communication import read_weight
from django.http import JsonResponse


def home(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'home.html', {'vehicles': vehicles})


def get_weight(request):
    weight = read_weight()
    return JsonResponse({'weight': weight})


def vehicle_entry(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.entry_weight = read_weight()
            vehicle.save()
            return redirect('vehicle_detail', pk=vehicle.pk)
    else:
        form = VehicleForm()
    return render(request, 'vehicle_entry.html', {'form': form})

def vehicle_exit(request, pk):
    vehicle = Vehicle.objects.get(pk=pk)
    if request.method == 'POST':
        vehicle.exit_weight = read_weight()
        vehicle.exit_time = timezone.now()
        vehicle.save()
        return redirect('vehicle_detail', pk=vehicle.pk)
    return render(request, 'vehicle_exit.html', {'vehicle': vehicle})

def vehicle_detail(request, pk):
    vehicle = Vehicle.objects.get(pk=pk)
    return render(request, 'vehicle_detail.html', {'vehicle': vehicle})

