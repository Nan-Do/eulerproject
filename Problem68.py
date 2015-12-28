from itertools import permutations, chain

def get_triplets_3(v):
    t1 = (v[3], v[2], v[1])
    t2 = (v[5], v[1], v[0])
    t3 = (v[4], v[0], v[2])
    
    m = min(v[3], v[5], v[4])
    if m == v[3]:
        return (t1, t2, t3)
    elif m == v[5]:
        return (t2, t3, t1)
    else:
        return (t3, t1, t2)

def get_triplets_5(v):
    t1 = (v[5], v[4], v[3])
    t2 = (v[9], v[3], v[2])
    t3 = (v[8], v[2], v[1])
    t4 = (v[7], v[1], v[0])
    t5 = (v[6], v[0], v[4])
    
    m = min(v[5], v[9], v[8], v[7], v[6])
    if m == v[5]:
        return (t1, t2, t3, t4, t5)
    elif m == v[9]:
        return (t2, t3, t4, t5, t1)
    elif m == v[8]:
        return (t3, t4, t5, t1, t2)
    elif m == v[7]:
        return (t4, t5, t1, t2, t3)
    else:
        return (t5, t1, t2, t3, t4)

answers = set()
for p in permutations(xrange(1, 11)):
    sums = map(sum, get_triplets_5(p))
    if all(x==sums[0] for x in sums):
        answers.add(''.join(map(str,
                                chain.from_iterable(get_triplets_5(p)))))

print max(answers)



