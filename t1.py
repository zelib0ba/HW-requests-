import os
import requests
os.system ('cls||clear')

url = 'https://superheroapi.com/api/2619421814940190/'
SuperHeroesNames = ['Hulk', 'Captain America', 'Thanos']

def get_hero_id (HeroName):
    """получаем ID супергероя"""
    search_url = f'{url}search/{HeroName}'
    response = requests.get(url=search_url, timeout=5)
    results = response.json()['results']
    for data in results:
        if data['name'] == HeroName:
            return data['id']

def get_hero_iq (id):
    """получаем IQ супергероя по ID номеру"""
    search_url = f'{url}{id}/powerstats'
    response = requests.get(url=search_url, timeout=1)
    result = response.json()
    return result['intelligence']

iq = 0
nero_name = ''
for key, name in enumerate (SuperHeroesNames):
    # print (f'Имя супер героя -> {SuperHeroesNames[key]}')
    # print (f'IQ супер героя -> {get_hero_iq(get_hero_id(name))}')
    hero_iq = get_hero_iq(get_hero_id(name))
    if int(hero_iq) > iq:
        iq = int(hero_iq)
        hero_name = name

print (f'Самый умный - {name} c iq {iq}')

