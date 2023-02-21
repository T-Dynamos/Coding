import random
import tests
from collections import deque


def gen_random_list(lenght: int, r1=10, r2=50) -> list:

    final_list = []

    def append_no():
        number = random.randint(r1, r2)
        if number not in final_list:
            final_list.append(number)
        else:
            append_no()

    for i in range(lenght):
        append_no()
    final_list.sort()
    return final_list


def print_lists(*args):

    big_list = []

    for i in range(10):
        l = deque(gen_random_list(20))
        rotated_times = random.randint(2, 19)
        l.rotate(rotated_times)
        big_list.append([list(l), rotated_times])
    return big_list


def get_rotated_times(lists):
    for i in lists:
        original_list = list(i[0])
        sorted_list = list(i[0])
        sorted_list.sort()
        max_value = sorted_list[-1]
        result = i[-1] == i[0].index(max_value) + 1
        print("Result = ", result)


print("\nElasped time :", tests.Run(get_rotated_times, print_lists()))
