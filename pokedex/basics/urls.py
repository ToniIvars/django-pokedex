from django.urls import path
from . import views

urlpatterns = [
    path('pokemon/<name>', views.pokemon, name='pokemon')
]