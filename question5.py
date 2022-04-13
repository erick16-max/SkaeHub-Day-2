import requests
from requests.exceptions import Timeout

url = "https://skaehub.com/"
def get_timeout_response(url):
    try:
        response = requests.get(url, timeout=1.0)
        return(response.status_code)
    except Timeout as err:
        raise err
    

print(get_timeout_response(url))

