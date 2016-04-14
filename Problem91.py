from math import sqrt

def euclide_distance((x_1, y_1), (x_2, y_2)):
    return sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)

def is_triangle_rectangle(p, q, origin=(0,0)):
    a = euclide_distance(p, origin)
    b = euclide_distance(q, origin)
    c = euclide_distance(p, q)

    c_1, c_2, h = sorted((a, b, c))
    #return sqrt((c_1 ** 2 + c_2 ** 2)) == h
    return abs(sqrt((c_1 ** 2 + c_2 ** 2)) - h) < 0.000001

def generate_tuples(n):
    a = ((x, y) for x in xrange(n+1)\
         for y in xrange(n+1))
    a.next()
    return a

n = 50
total = 0
visited_points = set()
for p in generate_tuples(n):
    visited_points.add(p)
    for q in generate_tuples(n):
        if q in visited_points:
            continue

        if is_triangle_rectangle(p, q):
            #print p,q
            total += 1
print total
