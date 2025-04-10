prime_nums = [2,3,5,7,11,13,17,19,23,29,31, 37, 41]

def factorial(number):
    data = {}.fromkeys(prime_nums)
    for num in  prime_nums:
        data[num] = [-1]
        while data[num][-1] != 0:
            data[num].append(
                int( number / (num**len(data[num]) ) )
            )
        data[num] = sum(data[num]) + 1 
    ans = 1
    print(data)
    for n in data.keys():
        ans = ans*(n**data[n])
    return ans

print(factorial(40))

import math 
print(math.factorial(40))
