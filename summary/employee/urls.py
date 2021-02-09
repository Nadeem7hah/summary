from django.urls import path
from .views import *
urlpatterns = [
    path('employees', get_employees),

]
