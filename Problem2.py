from itertools import ifilter, takewhile


def fib():
    a = 0
    b = 1
    while True:
        yield a + b
        temp = a + b
        a = b
        b = temp

print sum(ifilter(lambda x: (x % 2) == 0,
                  takewhile(lambda x: x <= 4000000,
                            fib())))
