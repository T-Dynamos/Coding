from timeit import default_timer as timer


def test(func, input, output):
    start = timer()
    result = func(input[0], input[1])
    end = timer()
    print("Result :", result, "Execution Time :", abs(start - end), "sec")
    return abs(start - end) / 100


def get_value_pos(original_list, value, high, low) -> int:
    if value > (high + low) // 2:
        return -1
    elif value < (high + low) // 2:
        return 1
    else:
        return 0


def get_index(original_list, value) -> int:
    """
    Binary tree method (Fast)
    """
    cards_flipped = 0
    if len(original_list) != 0:
        high = original_list[0]
        low = original_list[-1]
        mid = (high + low) // 2
    else:
        return -1

    while value in original_list:
        cards_flipped += 1
        #print("Bin method", cards_flipped)
        left = original_list[original_list.index(mid) - 1]
        right = original_list[original_list.index(mid) + 1]
        get_mid = lambda: original_list[
            (original_list.index(high) + original_list.index(low)) // 2
        ]
        if left == value:
            return original_list.index(left)
        elif right == value:
            return original_list.index(right)
        else:
            origin = get_value_pos(original_list, value, high, low)
            if origin == -1:
                mid = get_mid()
                low = mid
                mid = get_mid()
            elif origin == 1:
                mid = get_mid()
                high = mid
                mid = get_mid()
            elif origin == 0:
                return original_list.index(mid)
            else:
                return -1
    return -1


def get_index_br(original_list, value) -> int:
    """
    Bruteforce Method (slow)
    """
    cards_flipped = 0
    for i in original_list:
        cards_flipped += 1
        if i == value:
            return original_list.index(i)
    return -1


original_list = range(0, 1000000)[::-1]
value = 6

bin_method = test(get_index, (original_list, value), value)
br_method = test(get_index_br, (original_list, value), value)

if bin_method > br_method:
    print("Bruteforce method was fast")
else:
    print("Binary tree method was fast")
