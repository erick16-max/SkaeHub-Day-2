import json
import requests


url = "https://data.townofcary.org/api/v2/catalog/datasets/rdu-weather-history"
def get_dict_data(url):
    
    response = requests.get(url).text

    dict_data = json.loads(response)
    return dict_data

print(get_dict_data(url))