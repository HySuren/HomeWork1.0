def zeros(n):
    count = 0 
    while n != 0:
        count +=n // 5
        n = n //5
    return count


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
