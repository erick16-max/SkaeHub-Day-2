#Write a Python program to check if a given positive integer is a power of four.
import math
num = int(input('Enter the number:'))
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
        return False


print(is_power_of_four(num)) 


