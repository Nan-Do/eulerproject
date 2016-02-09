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
    # Initialize search values
    matrix_length = len(m)
    minimum = 711788
    paths = [(start, 0)]

    while len(paths):
        # Frontier state
        (x, y), value = paths.pop()
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
            paths.append(((new_x, new_y), new_value))
    return minimum


m = read_matrix('p081_matrix.txt')
print get_minimal_path(m)
