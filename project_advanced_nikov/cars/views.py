from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from project_advanced_nikov.accounts.mixins import CustomLoginRequiredMixin
from project_advanced_nikov.cars.forms import CarForm
from project_advanced_nikov.cars.models import Car


# Create your views here.
class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    template_name = 'cars/car_create.html'
    form_class = CarForm

    def get_success_url(self):
        return reverse_lazy("car_list", kwargs={"pk":self.request.user.pk})
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class CarDetailView(CustomLoginRequiredMixin, DetailView):
    model = Car
    template_name = 'cars/car_detail.html'
    context_object_name = 'car'

class CarUpdateView(CustomLoginRequiredMixin, UpdateView):
    model = Car
    template_name = 'cars/car_update.html'
    form_class = CarForm

    def get_success_url(self):
        return reverse_lazy("car_detail", kwargs={"pk":self.object.pk})


class CarDeleteView(CustomLoginRequiredMixin, DeleteView):
    model = Car
    template_name = 'cars/car_delete.html'

    def get_success_url(self):
        return reverse_lazy("car_list", kwargs={"pk":self.object.pk})

def car_list(request, pk):
    cars = Car.objects.filter(user_id=pk)
    if not request.user.is_authenticated or pk != request.user.pk:
        raise PermissionDenied
    return render(request, 'cars/car_list.html', {'cars': cars})