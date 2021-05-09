from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse

import json, requests
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

def get_abilities(data):
    abilities = []
    for d in data['abilities']:
        abilities_dict = {
            'name':d['ability']['name'].replace('-', ' '),
            'url':d['ability']['url'],
            'is_hidden': d['is_hidden']
        }
        # abilities_dict.update({})

        abilities.append(abilities_dict)

    return abilities

def get_types(data):
    types = [d['type'] for d in data['types']]
    return types

def get_stats(data):
    stats_values = [d['base_stat'] for d in data['stats']]
    stats_names = [d['stat']['name'] for d in data['stats']]
    
    return tuple(zip(stats_names, stats_values))

# Create your views here.
def pokemon(request, name):
    try:
        pokemon_id = json.load(open(BASE_DIR / 'pokemon_ids.json', 'r'))[name]
    except KeyError:
        messages.error(request, 'The Pokemon you are trying to find does not exist')
        return redirect('pokedex_index')

    res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/')   
    # evolution_res = requests.get(f'https://pokeapi.co/api/v2/evolution-chain/{pokemon_id}/')

    data = res.json()
    # evolution_data = evolution_res.json()

    sprite = data['sprites']['other']['official-artwork']['front_default']
    abilities = get_abilities(data)
    types = get_types(data)
    stats = get_stats(data)

    data = {'name':name, 'sprite':sprite, 'abilities':abilities, 'types':types, 'stats':stats}

    return render(request, 'basics/index.html', {'data':data})