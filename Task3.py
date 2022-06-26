def zeros(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return len(str(factorial)) - len(str(factorial).rstrip('0'))


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7