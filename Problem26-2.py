from __future__ import division
from operator import itemgetter

def make_division(n):
    x = 10
    while x < n:
        x *= 10
    while 1:
        r, x = divmod(x, n)
        yield r
        if x == 0:
            return
        while x < n:
            x *= 10


def cycle(n):
    num = str(1/n)
    if len(num) < 6:
        return 0
    num = num[2:]
    l = num[-2]
    if num.count(l) > 4:
        return 1
    print n, num
    for i in xrange(1, len(num)):
        if all(map(lambda x: x == '',
                   num.split(num[:i]))):
            return i

    return 0

print max(enumerate(map(cycle, xrange(1, 1001))), key=itemgetter(1))
