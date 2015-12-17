from itertools import count
from collections import Counter

c = Counter()
v = dict()
for x in (n ** 3 for n in count(start=1)):
    n = tuple(sorted(str(x)))
    c[n] += 1
    if n not in v:
        v[n] = x
    if c[n] == 5:
        print v[n]
        break
