import requests
import json


def get_superhero_dict():
    """
    Function gets all information about all heroes and returns the dictionary consisting of
    hero names and list of hero id and intelligence.
    :return:
    """
    url = f'https://akabab.github.io/superhero-api/api/all.json'
    request = requests.get(url)
    all_superheros = json.loads(request.text)
    return {hero['name']: [hero['id'], hero['powerstats']['intelligence']] for hero in all_superheros}


# def get_superhero_params(super_dict, superhero):
#     """
#     Additional function. Not used in exercise.
#     Function gets superhero's parameters from the API.
#     :param super_dict:
#     :param superhero:
#     :return:
#     """
#     super_num = super_dict[superhero]
#     url = f'https://akabab.github.io/superhero-api/api/powerstats/{super_num}.json'
#     request = requests.get(url)
#     params = json.loads(request.text)
#     return params


def get_the_most_intelligent_hero(superhero_list):
    """
    Function receives a list of superheroes, compares their intelligence and returns the name
    of the hero with the maximum intelligence value (if the intelligence of two heroes is equal,
    the function returns the hero that was earlier in the input list). If heroes are not in the API's
    json - the function returns message 'Heroes not found'.
    :param superhero_list:
    :return hero name or message 'Heroes not found':
    """
    most_intelligent = (None, 0)
    sph_dict = get_superhero_dict()
    for name in superhero_list:
        if name in sph_dict:
            if sph_dict[name][1] > most_intelligent[1]:
                most_intelligent = (name, sph_dict[name][1])
    return most_intelligent[0] if most_intelligent[0] else 'Heroes not found'


print(get_the_most_intelligent_hero(['Hulk', 'Captain America', 'Thanos']))

