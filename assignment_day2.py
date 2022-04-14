import math
import random
import requests
import requests
import statistics
import json

from requests.exceptions import Timeout



#Write a Python program to check if a given positive integer is a power of four.
def is_power_of_four(num):
    #check if positive
    if num > 0:
        #Find the log of the number to base 4 if power of four it will return whole number
        result = math.log(num,4)

        """
        since the result of the log returns a float but we can go around it using the method is.interger() 
        where if its decimal is zero e.g 4.0 then it will turn it as an interger but if it has many decimals
        e.g 4.1999 then it returns type of float
        """
        if result.is_integer():
            return True
        return False
    else:
        return 


#Write a Python program to check if a number is a perfect square.
def is_perfect_square(sqrt_num):
    """
    find the value you get when you square root then turn it into an interger and find
    its square if results match with the number you did its square root then its a perfect square
    """
    sqrt_value = math.sqrt(sqrt_num)

    return int(sqrt_value) ** 2 == sqrt_num #this should return True if perfect square


def guess_check (guess, random_number):
   #random_number = random.randrange(0,101)
    if guess == random_number:
        return "Hooray! You guessed right"
    elif guess > random_number:
        return f"The guessed number is higher than the random number {random_number}"
    elif guess < random_number:
        return f"The guessed number is lower than the random number {random_number}"
    else:
        return "enter a valid integer"




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

#getting response or connect timeout or read timeout
def get_timeout_response(url, timeout):
    timeout:int
    try:
        response = requests.get(url, timeout = timeout)
        return response.status_code
    except requests.exceptions.Timeout as err:
        raise err

def basic_stats(num_list):
    mean_list = statistics.mean(num_list)
    mode_list = statistics.mode(num_list)
    variance_list = statistics.variance(num_list)
    median_list = statistics.median(num_list)

    dict_stats = {
        'mean':mean_list,
        'mode':mode_list,
        'variance': variance_list,
        'medium':median_list
    }

    return dict_stats


def get_dict_data(url):
    
    response = requests.get(url).text

    dict_data = json.loads(response)
    return dict_data