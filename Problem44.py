from itertools import count, imap, islice

def take_pairs(l, n=5000000):
    previous = l.next()
    i = 0
    while i < n:
        current = l.next()
        yield (previous, current)
        previous = current
        i += 1
    raise StopIteration()

def modulus(n):
    if n >= 0:
        return n
    else:
        return -n

def pentagon_generator():
    return imap(lambda n: (n * ((3*n) - 1)) / 2, count(1))

pentagon_numbers = set(islice(pentagon_generator(), 5000))
p_n = list(islice(pentagon_generator(), 3000))

D = 1000000000000
while p_n:
    a = p_n.pop(0)
    for b in p_n:
        if (a + b) in pentagon_numbers and\
                modulus(b - a) in pentagon_numbers:
            if modulus(b - a) < D:
                D = (b - a)

print "The value of D is:", D
