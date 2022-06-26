from math import prod
from itertools import combinations_with_replacement as combo

def count_find_num(primesL, limit):
    data = []
    step = prod(primesL)
    next_steps = True
    places = 1
    factor_limit = limit // step
    if factor_limit:
        data.append(step)
    while next_steps:
        next_steps = False
        comb_gen = combo(primesL, places)
        for i in comb_gen:
            combination = prod(i)
            if combination <= factor_limit:
                data.append(combination * step)
                next_steps = True
        places += 1
    return [len(data), max(data)] if data else []


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]


primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []