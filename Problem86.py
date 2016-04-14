import heapq

def euclidean_distance((x, y, z), (x_1, y_1, z_1)):
    return ((x_1 - x) ** 2 + (y_1 - y) ** 2 + (z_1 - z) ** 2) ** 0.5

def is_a_positive_integer(x):
    return x == int(x) and x > 0


def generate_succesors(origin, destiny):
    (X, Y, Z) = origin
    (X1, Y1, Z1) = destiny
    successors = []
    for x in xrange(X, X1+1):
        for y in xrange(Y, Y1+1):
            for z in xrange(Z, Z1+1):
                current = (x, y, z)
                distance = euclidean_distance(origin, current)
                if is_a_positive_integer(distance):
                    successors.append((int(distance), current))
    return successors

def compute_routes(X, Y, Z):
    shortest_routes = {}
    destiny = (X, Y, Z)
    paths = [(0, (0,0,0))]

    while paths:
        distance, point = heapq.heappop(paths)
        
        if point not in shortest_routes or shortest_routes[point] < distance:
            shortest_routes[point] = distance
        else:
            continue

        successors = generate_succesors(point, destiny)
        for successor in successors:
            heapq.heappush(paths, successor)
    return shortest_routes

def c_r(origin, destiny):
    (X, Y, Z) = origin
    (X1, Y1, Z1) = destiny
    successors = []
    for x in xrange(X, X1+1):
        for y in xrange(Y, Y1+1):
            for z in xrange(Z, Z1+1):
                current = (x, y, z)
                distance = euclidean_distance(current, origin) +\
                           euclidean_distance(destiny, current)
                if is_a_positive_integer(distance) and current != destiny:
                    successors.append(current)
    return successors
 

def compute_routes_2(X, Y, Z):
    destiny = (X, Y, Z)
    points = [(0,0,0)]
    visited_points = set()

    while points:
        point = points.pop()
        successors = c_r(point, destiny)
        for successor in successors:
            if successor not in visited_points:
                visited_points.add(successor)
                points.append(successor)
    return visited_points

#print compute_routes(100, 100, 100)
#print generate_succesors((0,0,0), (10, 10, 10))
#print compute_routes_2(10, 10, 10)
#print compute_routes_2(10,10,10)
#
#print euclidean_distance((9,6,2), (10,10,10))
print len(compute_routes_2(100,100,100))
