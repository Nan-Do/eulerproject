from __future__ import division
from operator import itemgetter


def cycle(n):
    num = str(1/n)
    print n
    if len(num) < 6:
        return 0
    num = num[2:]
    l = num[-2]
    if num.count(l) > 4:
        return 1
    for i in xrange(1, len(num)):
        if all(map(lambda x: x == '',
                   num.split(num[:i]))):
            return i

    return 0

print max(enumerate(map(cycle, xrange(1, 1001))), key=itemgetter(1))
