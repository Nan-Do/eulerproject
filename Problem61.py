from itertools import permutations

def triangles(n):
    return n * ((n + 1) / 2)

def squares(n):
    return n * n

def pentagonals(n):
    return n * ((3 * n) - 1) / 2

def hexagonals(n):
    return n * ((2 * n) - 1)

def heptagonals(n):
    return n * ((5 * n) - 3) / 2

def octogonals(n):
   return n * ((3 * n) - 2)

t1 = []; t2 = {}
s1 = []; s2 = {}
p1 = []; p2 = {}
h1 = []; h2 = {}
hp1 = []; hp2 = {}
o1 = []; o2 = {}
for n in xrange(200):
    if triangles(n) >= 1000 and triangles(n) <= 10000:
        t1.append(triangles(n))
        t2[triangles(n)] = n

    if squares(n) >= 1000 and squares(n) <= 10000:
        s1.append(squares(n))
        s2[squares(n)] = n
        
    if pentagonals(n) >= 1000 and pentagonals(n) <= 10000:
        p1.append(pentagonals(n))
        p2[pentagonals(n)] = n

    if hexagonals(n) >= 1000 and hexagonals(n) <= 10000:
        h1.append(hexagonals(n))
        h2[hexagonals(n)] = n
        
    if heptagonals(n) >= 1000 and heptagonals(n) <= 10000:
        hp1.append(heptagonals(n))
        hp2[heptagonals(n)] = n
    
    if octogonals(n) >= 1000 and octogonals(n) <= 10000:
        o1.append(octogonals(n))
        o2[octogonals(n)] = n

def compute_sets(comb):
    def chunks(l, n):
        """Yield successive n-sized chunks from l."""
        for i in xrange(0, len(l)-1, 1):
            yield l[i:i+n]
            
    def join_elems(a, b):
        ans = []
        for elem1 in a:
            for elem2 in b:
                if elem1[-1] == elem2[0]:
                    ans.append(list(elem1) + [elem2[1]])
        
        return map(tuple, ans)
        
    def get_pairs(s, t):
        for elem1 in s:
            for elem2 in t:
                if (elem1 % 100) == (elem2 / 100):
                    yield (elem1, elem2)
    
    def get_data(v):
        if v == 'squares':
            return s1, s2
        elif v == 'triangles':
            return t1, t2
        elif v == 'pentagonals':
            return p1, p2
        elif v == 'hexagonals':
            return h1, h2
        elif v == 'heptagonals':
            return hp1, hp2
        elif v == 'octogonals':
            return o1, o2
        else:
            return None
        
    answers = []
    for elem in chunks(comb, 2):
        a,_ = get_data(elem[0])
        c,_ = get_data(elem[1])
        answers.append(list(get_pairs(a, c)))
        
    solutions = answers[0]
    for x in xrange(1, len(answers)):
        solutions = join_elems(solutions, answers[x])
        if len(solutions) == 0:
            return None
        
    dicts = map(lambda x: get_data(x)[1], comb) 
    for solution in solutions:
        if (solution[0] / 100) != (solution[-1] % 100): continue
        values = [dicts[x][y] for x,y in enumerate(solution)]
                
        print comb, solution,
        if len(set(values)) == len(comb):
            print sum(solution)
        
    return solutions
            
for p in permutations(['triangles', 'squares', 'pentagonals', 'hexagonals', 'heptagonals', 'octogonals']):
    compute_sets(p)
