from django.shortcuts import render, redirect
from .models import Sitter, Baby, Payment, Procurement
from .forms import SitterForm, BabyForm, PaymentForm, ProcurementForm
from django.urls import reverse_lazy

def sitter_create(request):
    if request.method == 'POST':
        form = SitterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sitter_create')  # Redirect to the same page after successful form submission
    else:
        form = SitterForm()
    return render(request, 'sitter_form.html', {'form': form})

def baby_create(request):
    if request.method == 'POST':
        form = BabyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('baby_create') # Redirect to the same page after successful form submission
    else:
        form = BabyForm()
    return render(request, 'baby_form.html', {'form': form})

def payment_create(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_create') # Redirect to the same page after successful form submission
    else:
        form = PaymentForm()
    return render(request, 'payment_form.html', {'form': form})

def procurement_create(request):
    if request.method == 'POST':
        form = ProcurementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('procurement_create') # Redirect to the same page after successful form submission
    else:
        form = ProcurementForm()
    return render(request, 'procurement_form.html', {'form': form})


def home(request):
    return render(request, 'base.html', {})