from django.urls import path
from . import views

urlpatterns = [
    path('<name>', views.move, name='move'),
]