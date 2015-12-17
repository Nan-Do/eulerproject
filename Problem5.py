from itertools import count, dropwhile


def is_divisible(n):
    return all(map(lambda x: (n % x) == 0, xrange(2, 21)))


print dropwhile(lambda x: not is_divisible(x), count(2, 2)).next()
