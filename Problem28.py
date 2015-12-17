from itertools import cycle, repeat, count

def sum_diagonals(m):
    n = len(m)
    return sum(m[i][i] + m[i][n-i-1] for i in xrange(n)) - 1

def gen_matrix(n):
    def get_path(center, path):
        sides = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}
        positions = [center]
        last = center
        for direction in path:
            element = sides[direction]
            last = (last[0] + element[0], last[1] + element[1])
            positions.append(last)
        return positions
    def fill_matrix(n, path):
        matrix = [[0] * n for _ in xrange(n)]
        for pos, value in zip(path, count(1)):
            matrix[pos[0]][pos[1]] = value
        return matrix

    # Get the sides and the center
    c = cycle(('R', 'D', 'L', 'U'))
    s = []
    for x in xrange(1, n):
        s += repeat(c.next(), x)
        s += repeat(c.next(), x)
    s += repeat(c.next(), (n-1))

    return fill_matrix(n, get_path((n/2, n/2), s))

print sum_diagonals(gen_matrix(1001))
