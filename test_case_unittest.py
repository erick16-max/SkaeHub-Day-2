from email import message
from random import random
from typing import Dict
import unittest

from requests import ConnectTimeout, ReadTimeout
from assignment_day2 import is_power_of_four, is_perfect_square, guess_check, get_data, get_timeout_response, basic_stats, get_dict_data


class TestFunc(unittest.TestCase):

    def setUp(self):
        pass
        
    #testing if the positive number is a power of four
    def test_is_power_of_four(self):
        
        self.assertTrue(is_power_of_four(64), None)
        self.assertFalse(is_perfect_square(32), None)
        self.assertIsInstance(is_perfect_square(16), int)

    #testing a perfect square
    def test_is_perfect_square(self):
        self.assertTrue(is_perfect_square(25), None)
        self.assertFalse(is_perfect_square(78), None)
    
    #check if the guessed number equal to random number
    def test_guess_check_right(self):
        random_number = 20
        guess = 20
        message = "Hooray! You guessed right"
        self.assertEqual(guess_check(guess, random_number), message)

    #check if the guessed number is higher
    def test_guess_check_lower(self):
        random_number = 20
        guess = 50
        message = f"The guessed number is higher than the random number {random_number}"
        self.assertEqual(guess_check(guess, random_number), message)
    
    #check if the guessed number is lower
    def test_guess_check_lower(self):
        random_number = 80
        guess = 50
        message = f"The guessed number is lower than the random number {random_number}"
        self.assertEqual(guess_check(guess, random_number), message)
    
    #testing for the connection timeout
    def test_connectTimeout_response(self):
        timeout = (0.1, 3.0)
        with self.assertRaises(ConnectTimeout):
           get_timeout_response("https://skaehub.com/", timeout)
    
    #testing for the read timeout
    def test_readTimeout_response(self):
        timeout = (2.0, 0.1)
        with self.assertRaises(ReadTimeout):
           get_timeout_response("https://skaehub.com/", timeout)

    #basic statistics on a list to return a dictionary
    def test_get_stats(self):
        list_items = [20,90,8,10,45,24]
        dict_data = {'mean': 32.833333333333336, 'mode': 20, 'variance': 959.3666666666667, 'medium': 22.0}
        self.assertEqual(basic_stats(list_items), dict_data)
    
    #Checking if the method returns a dictionary after parsing the json data from  API
    def test_get_dict_data(self):
        url = "https://data.townofcary.org/api/v2/catalog/datasets/rdu-weather-history"
        self.assertIsInstance(get_dict_data(url), Dict)
          


if __name__ == '__main__':
    unittest.main()