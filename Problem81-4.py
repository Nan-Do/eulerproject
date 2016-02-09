import heapq

def read_matrix(file_name):
    matrix = []
    with open(file_name) as f:
        for line in f.readlines():
            row = map(int, line.split(','))
            matrix.append(row)
    return matrix


def get_minimal_path(m,
                     ways=[(0, 1), (1, 0)],
                     start=(0, 0)):
    matrix_length = len(m) - 1
    costs_matrix = [ [0] * (matrix_length+1) for _ in xrange(matrix_length+1) ]
    level = [(0, (0,0))]
    successors = []

    while len(level):
        cost, (x, y) = heapq.heappop(level)
        new_cost = cost + m[x][y]

        # Check costs matrix
        if costs_matrix[x][y] == 0 or new_cost <= costs_matrix[x][y]:
            costs_matrix[x][y] = new_cost
        else:
            continue


        # Successors
        for (delta_x, delta_y) in ways:
            if (x + delta_x) == len(m) or\
               (y + delta_y) == len(m):
                continue
            
            position = (x + delta_x, y + delta_y)
            heapq.heappush(level, (new_cost, position))

    return costs_matrix[matrix_length][matrix_length]

#m = [ [131, 673, 234, 103,  18],
#      [201,  96, 342, 965, 150],
#      [630, 803, 746, 422, 111],
#      [537, 699, 497, 121, 956],
#      [805, 732, 524,  37, 331]]
m = read_matrix('p081_matrix.txt')
print get_minimal_path(m)
