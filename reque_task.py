import requests
from prof_py_decor import logger

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'

source = requests.get(url)
hero_list = source.json()
intelligence = {}
intel = []

@logger
def intel_hero(name):
    for hero_info in hero_list:
        hero_name = hero_info['name']
        hero_powerstats = hero_info['powerstats']
        if hero_name in name:
            hero_com = {hero_name: hero_powerstats['intelligence']}
            intelligence.update(hero_com)
            intel.append(hero_powerstats['intelligence'])


list_of_hero = ['Hulk', 'Thanos', 'Captain America', 'A-Bomb', 'Yoda', 'Apocalypse']

intel_hero(list_of_hero)
sorted_tuples = sorted(intelligence.items(), key=lambda item: item[1])
sorted_dict = {key: value for key, value in sorted_tuples}
result = list(sorted_dict)
res_for_int = sorted(intel)

print(f'Самый умный: {result[-1]} - {res_for_int[-1]}')
