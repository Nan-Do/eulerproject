import heapq

def read_matrix(file_name):
    matrix = []
    with open(file_name) as f:
        for line in f.readlines():
            row = map(int, line.split(','))
            matrix.append(row)
    return matrix


def estimated_cost((x, y), m):
    cost = 0
    for y_1 in xrange(y, len(m)):
        cost += m[x][y_1]
    for x_1 in xrange(x+1, len(m)):
        cost += m[x_1][-1]
    return cost

def heap_key(x):
    return x[1] + x[2]

def get_minimal_path(m,
                     ways=[(0, 1), (1, 0)],
                     start=(0, 0)):
    # Initialize search values
    matrix_length = len(m)
    minimum = -1
    element = (start, 0, estimated_cost(start, m))
    paths = [(heap_key(element), element)]

    while len(paths):
        # Frontier state
        (x, y), value, estimated = heapq.heappop(paths)[1]
        new_value = value + m[x][y]

        # Prune useles paths
        if minimum != -1 and new_value >= minimum:
            continue

        # Goal state
        if x == y == (matrix_length - 1):
            print 'Goal!!!!!!!!!!!'
            if minimum == -1 or new_value < minimum:
                print 'New minimum', new_value
                minimum = new_value
                continue

        # Successors
        for (delta_x, delta_y) in ways:
            new_x = x + delta_x
            new_y = y + delta_y
            if new_x == matrix_length or\
               new_y == matrix_length:
                   continue
            new_position = (new_x, new_y)
            new_element = (new_position, new_value, estimated_cost(new_position, m))
            heapq.heappush(paths,
                           (heap_key(new_element), new_element))
    return minimum

#m = [ [131, 673, 234, 103,  18],
#      [201,  96, 342, 965, 150],
#      [630, 803, 746, 422, 111],
#      [537, 699, 497, 121, 956],
#      [805, 732, 524,  37, 331]]
m = read_matrix('p081_matrix.txt')
print get_minimal_path(m)
