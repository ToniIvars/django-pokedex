from django.shortcuts import render, redirect
from django.contrib import messages

import json, requests

# Create your views here.
def move(request, name):
    res = requests.get(f'https://pokeapi.co/api/v2/move/{name}/')   

    if res.status_code != 200:
        messages.error(request, 'The move you are trying to find does not exist')
        return redirect('pokedex_index')

    data = res.json()

    effect = data['effect_entries'][0]['effect']
    if '$effect_chance' in effect:
        effect = effect.replace('$effect_chance', str(data['effect_chance']))

    move_data = {
        'accuracy': data['accuracy'],
        'power': data['power'],
        'pp': data['pp'],
        'type': data['type']['name'],
        'category': data['damage_class']['name'],
        'description': [entry['flavor_text'].replace('\n', ' ') for entry in data['flavor_text_entries'] if entry['language']['name'] == 'en' and  entry['version_group']['name'] =='ultra-sun-ultra-moon'][0],
        'effect': effect
    }
    
    data = {'name':name.capitalize().replace('-', ' '), 'move_data':move_data}

    return render(request, 'moves/move.html', {'data':data})