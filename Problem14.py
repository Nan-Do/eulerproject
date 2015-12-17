from operator import itemgetter


def Collatz(n):
    count = 1
    x = n
    while x != 1:
        if (x % 2) == 0:
            x /= 2
        else:
            x = (3 * x) + 1

        count += 1
    return count

print max(enumerate(map(Collatz, xrange(1, 1000000)), start=1),
          key=itemgetter(1))
