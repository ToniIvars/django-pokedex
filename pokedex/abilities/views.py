from django.shortcuts import render, redirect
from django.contrib import messages

import json, requests

# Create your views here.
def ability(request, name):
    res = requests.get(f'https://pokeapi.co/api/v2/ability/{name}/')   

    if res.status_code != 200:
        messages.error(request, 'The ability you are trying to find does not exist')
        return redirect('pokedex_index')

    data = res.json()

    move_data = {
        'description': [entry['flavor_text'].replace('\n', ' ') for entry in data['flavor_text_entries'] if entry['language']['name'] == 'en' and entry['version_group']['name'] =='ultra-sun-ultra-moon'][0],
        'effect': [effect['effect'] for effect in data['effect_entries'] if effect['language']['name'] == 'en'][0]
    }
    
    data = {'name':name.capitalize().replace('-', ' '), 'move_data':move_data}

    return render(request, 'abilities/ability.html', {'data':data})