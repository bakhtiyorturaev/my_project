from django.urls import path
from .views import noutbuks_list, get_noutbuks_info

urlpatterns = [
    path('', noutbuks_list, name='list-noutbuk'),
    path('<int:pk>/', get_noutbuks_info, name='detail-noutbuk'),
]