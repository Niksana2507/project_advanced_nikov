from django.urls import path

from project_advanced_nikov.cars.views import CarDetailView, CarCreateView, CarUpdateView, CarDeleteView, car_list

urlpatterns = (
    path('', car_list, name='car_list'),
    path('create/', CarCreateView.as_view(), name='car_create'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('cars/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    path('cars/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
)