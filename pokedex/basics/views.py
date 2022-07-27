from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse

import json, requests

def get_evolution_chain(pokemon):
    pokemon_name = pokemon.title().replace('-', ' ')
    if pokemon_name == 'Farfetchd':
        pokemon_name = "Farfetch'd"
    if pokemon_name == 'Sirfetchd':
        pokemon_name = "Sirfetch'd"
    evolution_file = json.load(open('evolutions.json', 'r'))

    for evo in evolution_file:
        if pokemon_name in evo['chain']:            
            return evo

def get_abilities(data):
    abilities = []
    for d in data['abilities']:
        abilities_dict = {
            'name':d['ability']['name'].replace('-', ' '),
            'url':d['ability']['url'],
            'is_hidden': d['is_hidden']
        }

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
    res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}/')   

    if res.status_code != 200:
        messages.error(request, 'The Pokemon you are trying to find does not exist')
        return redirect('pokedex_index')

    data = res.json()

    sprite = data['sprites']['other']['official-artwork']['front_default']
    abilities = get_abilities(data)
    types = get_types(data)
    stats = get_stats(data)
    evolution_chain = get_evolution_chain(name)

    name = name.title().replace('-', ' ')
    name = "Farfetch'd" if name == 'Farfetchd' else "Sirfetch'd" if name in ('Farfetchd', 'Sirfetchd') else name

    data = {'name':name, 'sprite':sprite, 'abilities':abilities, 'types':types, 'stats':stats, 'evolution_chain':evolution_chain}

    return render(request, 'basics/index.html', {'data':data})

def moves(request, name):
    res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}/')   

    if res.status_code != 200:
        messages.error(request, 'The Pokemon you are trying to find does not exist')
        return redirect('pokedex_index')
        
    data = res.json()

    sprite = data['sprites']['other']['official-artwork']['front_default']

    gen_games = {
        ('red-blue', 'yellow'): 'gen_1',
        ('gold-silver', 'crystal'): 'gen_2',
        ('ruby-sapphire', 'firered-leafgreen', 'emerald'): 'gen_3',
        ('diamond-pearl', 'platinum', 'heartgold-soulsilver'): 'gen_4',
        ('black-white', 'black-2-white-2'): 'gen_5',
        ('x-y', 'omega-ruby-alpha-sapphire'): 'gen_6',
        ('sun-moon', 'ultra-sun-ultra-moon'): 'gen_7'
    }

    moves = {
        'gen_1': {'level_up':[], 'egg':[], 'machine':[], 'tutor':[]},
        'gen_2': {'level_up':[], 'egg':[], 'machine':[], 'tutor':[]},
        'gen_3': {'level_up':[], 'egg':[], 'machine':[], 'tutor':[]},
        'gen_4': {'level_up':[], 'egg':[], 'machine':[], 'tutor':[]},
        'gen_5': {'level_up':[], 'egg':[], 'machine':[], 'tutor':[]},
        'gen_6': {'level_up':[], 'egg':[], 'machine':[], 'tutor':[]},
        'gen_7': {'level_up':[], 'egg':[], 'machine':[], 'tutor':[]}
    }

    for move in data['moves']:      
        move_name = move['move']['name'].capitalize().replace('-', ' ')
        information = json.load(open('moves_information.json', 'r'))[str(move['move']['url'].split('/')[-2])]

        for details in move['version_group_details']:
            level_learned = details['level_learned_at']
            learn_method = details['move_learn_method']['name'].replace('-', '_')
            game = details['version_group']['name']

            try:
                generation = [gen for games, gen in gen_games.items() if game in games][0]

                move_data = {
                    'name': move_name,
                    'level': level_learned,
                    'accuracy': information['accuracy'],
                    'power': information['power'],
                    'pp': information['pp'],
                    'type': information['type'],
                    'category': information['category']
                }
                
                if move_data not in moves[generation][learn_method]:
                    moves[generation][learn_method].append(move_data)
            
            except IndexError:
                pass

    name = name.title().replace('-', ' ')
    name = "Farfetch'd" if name == 'Farfetchd' else "Sirfetch'd" if name in ('Farfetchd', 'Sirfetchd') else name

    data = {'name':name.lower(), 'sprite':sprite, 'moves':tuple(zip([f'gen-{num+1}' for num in range(7)], [moves[f'gen_{num+1}'] for num in range(7)]))}

    return render(request, 'basics/moves.html', {'data':data})
