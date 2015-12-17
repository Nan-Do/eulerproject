from itertools import imap, count, islice

def pentagon_generator():
    return imap(lambda n: (n * ((3*n) - 1)) / 2, count(1))

def triangle_generator():
    return imap(lambda n: (n * (n + 1)) / 2, count(1))

def hexagonal_generator():
    return imap(lambda n: (n * ((2 * n) - 1)), count(1))


triangular_numbers = set(islice(triangle_generator(), 100000))
pentagon_numbers = set(islice(pentagon_generator(), 100000))
hexagonal_numbers = set(islice(hexagonal_generator(), 100000))


a = triangular_numbers & pentagon_numbers & hexagonal_numbers
print a
