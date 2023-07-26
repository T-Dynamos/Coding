import math
array = [1,2,3,4,6,7]
len_digit = 3 
even = True 

def calc_combinations(len_digit , array, even):
    even_numbers = [_ % 2 for _ in array].count(0)
    return math.factorial(len(array)-1) / math.factorial(len(array) - 1 - (len_digit - 1))  * even_numbers

print(calc_combinations(len_digit, array, even))
