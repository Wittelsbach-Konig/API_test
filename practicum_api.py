from pprint import pprint

import requests

url = 'https://practicum.yandex.ru/api/user_api/homework_statuses/'
headers = {'Authorization': 'OAuth <token>'}
payload = {'from_date': 1675209600}

# Делаем GET-запрос к эндпоинту url с заголовком headers и параметрами params
homework_statuses = requests.get(url, headers=headers, params=payload)

# Печатаем ответ API в формате JSON
# print(homework_statuses.text)

# А можно ответ в формате JSON привести к типам данных Python и напечатать и его
pprint(homework_statuses.json())
