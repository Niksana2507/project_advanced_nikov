from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from project_advanced_nikov.cars.forms import CarForm
from project_advanced_nikov.cars.models import Car


# Create your views here.
class CarCreateView(CreateView):
    model = Car
    template_name = 'cars/car_create.html'
    form_class = CarForm
    success_url = reverse_lazy('car_list')

class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car_detail.html'
    context_object_name = 'car'

class CarUpdateView(UpdateView):
    model = Car
    template_name = 'cars/car_update.html'
    form_class = CarForm
    success_url = reverse_lazy('car_list')

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'cars/car_delete.html'
    success_url = reverse_lazy('car_list')

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})