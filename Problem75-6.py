from collections import deque
from itertools import count

def gen_primitive_triplets(seed=(3, 4, 5), limit=1500000, f=sum):
    def mult_mat_vec(m, v):
        res = []
        for x in xrange(len(v)):
            a = 0
            for y in xrange(len(v)):
                a += m[x][y] * v[y]
            res.append(a)
        return tuple(res)

    queue = deque()
    queue.append(seed)
    while len(queue):
        element = queue.popleft()
        value = f(element)
        if value > limit:
            continue
        queue.append(mult_mat_vec([[1, -2, 2], 
                                   [2, -1, 2], 
                                   [2, -2, 3]],
                                  element))
        queue.append(mult_mat_vec([[1, 2, 2],
                                   [2, 1, 2],
                                   [2, 2, 3]],
                                  element))
        queue.append(mult_mat_vec([[-1, 2, 2],
                                   [-2, 1, 2],
                                   [-2, 2, 3]],
                                  element))

        yield element


sums = set()
duplicated = set()
limit = 1500000
#f = lambda x: x[2]
f = sum 
for triplet in gen_primitive_triplets(limit=limit, f=f):
    for x in count():
        new_triplet = tuple(map(lambda y: y * x, triplet))
        s = f(new_triplet)
        if s > limit:
            break
        if s in sums:
            duplicated.add(s)
        sums.add(s)

print len(sums.difference(duplicated))
