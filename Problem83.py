import heapq

def read_matrix(file_name):
    matrix = []
    with open(file_name) as f:
        for line in f.readlines():
            row = map(int, line.split(','))
            matrix.append(row)
    return matrix


def get_minimal_path(m,
                     ways=[(0, 1), (1, 0), (-1, 0), (0, -1)],
                     start=(0, 0)):
    costs_matrix = [ [0] * len(m) for _ in xrange(len(m)) ]
    paths = [(0, start)]

    while paths:
        cost, (x, y) = heapq.heappop(paths)
        new_cost = cost + m[x][y]

        # Check costs matrix
        if costs_matrix[x][y] == 0 or new_cost <= costs_matrix[x][y]:
            costs_matrix[x][y] = new_cost
        else:
            continue


        # Successors
        for (delta_x, delta_y) in ways:
            if (x + delta_x) == len(m) or\
               (y + delta_y) == len(m) or\
               (x + delta_x) < 0 or\
               (y + delta_y) < 0:
                continue
            
            position = (x + delta_x, y + delta_y)
            heapq.heappush(paths, (new_cost, position))

    return costs_matrix[len(m)-1][len(m)-1]

#m = [ [131, 673, 234, 103,  18],
#      [201,  96, 342, 965, 150],
#      [630, 803, 746, 422, 111],
#      [537, 699, 497, 121, 956],
#      [805, 732, 524,  37, 331]]
m = read_matrix('p081_matrix.txt')
print get_minimal_path(m)
