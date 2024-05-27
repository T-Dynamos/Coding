# I am in love with dynamic programming!

def get_lcm(*numbers) -> dict:
    side_factors = []
    steps = [list(numbers)]
    i = 2
    while True:
        steps += [[0] * len(numbers)]
        did_step = False
        for count, n in enumerate(steps[-2]):
            if n % i == 0:
                did_step = True
                steps[-1][count] = n // i
            else:
                steps[-1][count] = n
        if not did_step:
            steps = steps[:-1]
            i += 1
        else:
            side_factors.append(i)
        if steps[-1] == [1] * len(numbers):
            break
    return {"steps": steps, "side_factors": side_factors}


def get_hcf(*numbers) -> list:
    numbers = list(numbers)
    numbers.sort()
    chunked_numbers = [
        [numbers[_], (numbers[_ + 1] if _ + 1 < len(numbers) else None)]
        for _ in range(0, len(numbers), 2)
    ]
    solved_chunks = [0] * len(chunked_numbers)
    for count, n in enumerate(chunked_numbers):
        if n[1] == None:
            n = [solved_chunks[count-1], n[0]]
        rem = n[0]
        while True:
            if n[1] % rem == 0:
                break
            rem = n[1] % rem
        solved_chunks[count] = rem
    return solved_chunks


print(get_lcm(6939))
