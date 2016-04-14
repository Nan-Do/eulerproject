def euclidean_distance((x, y, z), (x_1, y_1, z_1)):
    return ((x_1 - x) ** 2 + (y_1 - y) ** 2 + (z_1 - z) ** 2) ** 0.5

def is_a_positive_integer(x, error=0.001):
    #return x == int(x) and x > 0
    return abs(x - int(x)) < error

def compute_distance(origin, destiny, point):
    a = euclidean_distance(point, origin)
    b = euclidean_distance(destiny, point)
    return a + b

def minimum_integer_route(destiny, origin=(0,0,0), increment=0.01):
    temp_x, temp_y, temp_z = origin
    X, Y, Z = destiny
    minimum_distance = sum(destiny)

    while temp_x < X:
        point = (temp_x, 0, Z)
        distance = compute_distance(origin, destiny, point)
        if distance < minimum_distance:
            minimum_distance = distance
        temp_x += increment

    while temp_z < Z:
        point = (0, Y, temp_z)
        distance = compute_distance(origin, destiny, point)
        if distance < minimum_distance:
            minimum_distance = distance
        temp_z += increment

    while temp_y < Y:
        point = (X, temp_y, 0)
        distance = compute_distance(origin, destiny, point)
        if distance < minimum_distance:
            minimum_distance = distance
        temp_y += increment

    return minimum_distance

def minimum_integer_route_2(destiny, increment=0.01):
    origin = (0,0,0)
    X, Y, Z = destiny
    minimum_distance = sum(destiny)

    temp = int(euclidean_distance((0, Y, Z), origin))
    while temp > Y: 
        z = (temp ** 2 - Y ** 2) ** 0.5
        distance = compute_distance(origin, destiny, (0, Y, z))
        if distance <= minimum_distance:
            minimum_distance = distance
        temp -= increment

    temp = int(euclidean_distance((0, Y, Z), origin))
    while temp > Z:
        y = (temp ** 2 - Z ** 2) ** 0.5
        distance = compute_distance(origin, destiny, (0, y, Z))
        if distance <= minimum_distance:
            minimum_distance = distance
        temp -= increment 

    temp = int(euclidean_distance((X,Y,0), origin))
    while temp > X:
        y = (temp ** 2 - X ** 2) ** 0.5
        distance = compute_distance(origin, destiny, (X, y, 0))
        if distance <= minimum_distance:
            minimum_distance = distance
        temp -= increment

    return minimum_distance

def compute_integer_routes(M):
    total = 0
    for x in xrange(1, M):
        for y in xrange(x, M):
            for z in xrange(y, M):
                d = minimum_integer_route_2((x, y, z))
                if is_a_positive_integer(d):
                    print (x, y, z)
                    total += 1
    return total


#print compute_routes(3, 5, 6)
#print minimum_integer_route((100, 100, 100))
#print c_r_2(100, 100, 100)
print compute_integer_routes(99)
#print minimum_integer_route_2((3,5,6))
