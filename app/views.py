# views.py
from django.utils import timezone
from django.shortcuts import render, redirect
from .models import Vehicle
from .serial_communication import read_weight
from django.http import JsonResponse

'''
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

'''

from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehicle
from .forms import VehicleEntryForm, VehicleUpdateForm

def home(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'home.html', {'vehicles': vehicles})

def vehicle_entry(request):
    if request.method == 'POST':
        form = VehicleEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VehicleEntryForm()
    return render(request, 'vehicle_entry.html', {'form': form})


def vehicle_update(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        form = VehicleUpdateForm(request.POST, instance=vehicle)
        if form.is_valid():
            vehicle = form.save(commit=False)
            if vehicle.exit_weight and not vehicle.exit_time:
                vehicle.exit_time = timezone.now()
            if vehicle.entry_weight and vehicle.exit_weight:
                vehicle.net_weight = vehicle.exit_weight - vehicle.entry_weight
            vehicle.save()
            return redirect('home')
    else:
        form = VehicleUpdateForm(instance=vehicle)
    return render(request, 'vehicle_update.html', {'form': form, 'vehicle': vehicle})


def get_weight(request):
    # Dummy implementation for fetching weight
    weight = 1234.56
    return JsonResponse({'weight': weight})

def vehicle_detail(request, pk):
    vehicle = Vehicle.objects.get(pk=pk)
    return render(request, 'vehicle_detail.html', {'vehicle': vehicle})

def vehicle_delete(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    vehicle.delete()
    return redirect('home')