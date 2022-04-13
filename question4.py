import requests


def get_data(url):
    #getting content and text from url
    url = "https://skaehub.com/"
    try:
        response = requests.get(url)

        response_text = response.text
        response_content = response.content

       

        #extracting raw data(bytes) in an api
        url_raw = "https://api.github.com/events"
        response_api = requests.get(url_raw, stream=True)
        response_raw = response_api.raw
        

        return response_content, response_text, response_raw
        
    except requests.exceptions.RequestException as err:
        return err

