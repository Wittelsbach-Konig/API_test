import requests

from pprint import pprint


if __name__ == '__main__':
    response = requests.get('https://swapi.dev/api/starships/9/')
    #  response = response.json()
    #  print(response.json().get('name'))
    #  А если запросить несуществующий ключ словаря?
    print(response.json().get('my_name', 'Darth Vader'))
    pprint(response.json())
    params_dict = {'search': 'luke'}
    response = requests.get('https://swapi.dev/api/people/', params=params_dict)
    characters = response.json().get('results')[0]
    pprint(characters)