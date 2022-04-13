#Write a Python program to check if a number is a perfect square.
import math

num = int(input("Enter number:"))
def is_perfect_square(sqrt_num):
    """
    find the value you get when you square root then turn it into an interger and find
    its square if results match with the number you did its square root then its a perfect square
    """
    sqrt_value = math.sqrt(sqrt_num)

    return int(sqrt_value) ** 2 == sqrt_num #this should return True if perfect square

if is_perfect_square(num):
    print(f'{num} is a perfect spuare')
else:
    print(f'{num} not a perfect square')