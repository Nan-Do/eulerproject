from itertools import permutations

def list_to_int(a):
    return sum(map(lambda x: x[0]*(10**x[1]), zip(a, xrange(len(a)-1, -1, -1))))


result = 0
for p in permutations(xrange(0, 10), 10):
    if p[0] == 0: continue
    if list_to_int(p[1:4]) % 2 != 0: continue
    if list_to_int(p[2:5]) % 3 != 0: continue
    if list_to_int(p[3:6]) % 5 != 0: continue
    if list_to_int(p[4:7]) % 7 != 0: continue
    if list_to_int(p[5:8]) % 11 != 0: continue
    if list_to_int(p[6:9]) % 13 != 0: continue
    if list_to_int(p[7:10]) % 17 != 0: continue

    n = list_to_int(p)
    print n, p
    result += n

print result
