from django.urls import path
from . import views

urlpatterns = [
    path('<name>', views.pokemon, name='pokemon'),
    path('<name>/moves', views.moves, name='moves')
]