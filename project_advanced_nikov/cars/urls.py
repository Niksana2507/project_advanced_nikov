from django.urls import path

from project_advanced_nikov.cars.views import CarDetailView, CarCreateView, CarUpdateView, CarDeleteView, car_list

urlpatterns = (
    path('<int:pk>/', car_list, name='car_list'),
    path('create/', CarCreateView.as_view(), name='car_create'),
    path('<int:pk>/detail/', CarDetailView.as_view(), name='car_detail'),
    path('<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    path('<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
)