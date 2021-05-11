from django.shortcuts import render, redirect
from django.contrib import messages

import json, requests

# Create your views here.
def move(request, name):
    data = {'name':name}
    return render(request, 'moves/move.html', {'data':data})