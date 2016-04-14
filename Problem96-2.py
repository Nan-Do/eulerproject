from itertools import product

#sudoku = [ [0, 0, 3, 0, 2, 0, 6, 0, 0],
#           [9, 0, 0, 3, 0, 5, 0, 0, 1],
#           [0, 0, 1, 8, 0, 6, 4, 0, 0],
#           [0, 0, 8, 1, 0, 2, 9, 0, 0],
#           [7, 0, 0, 0, 0, 0, 0, 0, 8],
#           [0, 0, 6, 7, 0, 8, 2, 0, 0],
#           [0, 0, 2, 6, 0, 9, 5, 0, 0],
#           [8, 0, 0, 2, 0, 3, 0, 0, 9],
#           [0, 0, 5, 0, 1, 0, 3, 0, 0] ]

#sudoku = [ [2, 0, 0, 0, 8, 0, 3, 0, 0], 
#           [0, 6, 0, 0, 7, 0, 0, 8, 4],
#           [0, 3, 0, 5, 0, 0, 2, 0, 9],
#           [0, 0, 0, 1, 0, 5, 4, 0, 8],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [4, 0, 2, 7, 0, 6, 0, 0, 0],
#           [3, 0, 1, 0, 0, 7, 0, 4, 0],
#           [7, 2, 0, 0, 4, 0, 0, 6, 0],
#           [0, 0, 4, 0, 1, 0, 0, 0, 3] ]


sudoku = [ [1, 0, 0, 9, 2, 0, 0, 0, 0],
           [5, 2, 4, 0, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 7, 0],
           [0, 5, 0, 0, 0, 8, 1, 0, 2],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [4, 0, 2, 7, 0, 0, 0, 9, 0],
           [0, 6, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 3, 0, 9, 4, 5],
           [0, 0, 0, 0, 7, 1, 0, 0, 6] ]


#sudoku_solved = [ [4, 8, 3, 9, 2, 1, 6, 5, 7],
#                  [9, 6, 7, 3, 4, 5, 8, 2, 1],
#                  [2, 5, 1, 8, 7, 6, 4, 9, 3],
#                  [5, 4, 8, 1, 3, 2, 9, 7, 6],
#                  [7, 2, 9, 5, 6, 4, 1, 3, 8],
#                  [1, 3, 6, 7, 9, 8, 2, 4, 5],
#                  [3, 7, 2, 6, 8, 9, 5, 1, 4],
#                  [8, 1, 4, 2, 5, 3, 7, 6, 9],
#                  [6, 9, 5, 4, 1, 7, 3, 8, 2] ]
                  

def get_empty_squares(s):
    positions = []
    for x in xrange(len(s)):
        for y in xrange(len(s)):
            if s[x][y] == 0:
                positions.append((x, y))
    return positions

def get_posible_values((p_x, p_y), s):
    row = [] 
    column = []
    square = []
    for x in xrange(len(s)):
        if s[p_x][x] != 0:
            row.append(s[p_x][x])
        if s[x][p_y] != 0:
            column.append(s[x][p_y])
    if p_x < 3: start_x = 0
    elif p_x < 6: start_x = 3
    else: start_x = 6
    if p_y < 3: start_y = 0
    elif p_y < 6: start_y = 3
    else: start_y = 6
    for x in xrange(start_x, start_x + 3):
        for y in xrange(start_y, start_y + 3):
            if s[x][y] != 0:
                square.append(s[x][y])
    return set(xrange(1, 10)).difference(set(row).union(column).union(square))

def is_a_valid_sudoku(s):
    squares = [set() for _ in xrange(9)]
    for x in xrange(9):
        row = set()
        column = set()
        for y in xrange(9):
            row.add(s[x][y])
            column.add(s[y][x])
            if x < 3:
                if y < 3: squares[0].add(s[x][y])
                elif y < 6: squares[1].add(s[x][y])
                else: squares[2].add(s[x][y])
            elif x < 6:
                if y < 3: squares[3].add(s[x][y])
                elif y < 6: squares[4].add(s[x][y])
                else: squares[5].add(s[x][y])
            else:
                if y < 3: squares[6].add(s[x][y])
                elif y < 6: squares[7].add(s[x][y])
                else: squares[8].add(s[x][y])
        if 0 in row or 0 in column or len(row) != 9 or len(column) != 9:
            return False
    for v in squares:
        if 0 in v or len(v) != 9:
            return False

    return True


def fill_unique_positions(sudoku):
    while (not is_a_valid_sudoku(sudoku)):
        positions = get_empty_squares(sudoku)
        possible_values = map(lambda p: get_posible_values(p, sudoku),
                              positions)
        unique_positions = filter(lambda x: len(x[1]) == 1,
                                  zip(positions, possible_values))
        if len(unique_positions) == 0:
            break
        for (x, y), v in unique_positions:
            sudoku[x][y] = v.pop()
    return sudoku

def solve_sudoku(sudoku):
    def update_sudoku(sudoku, solving_stack):
        (x, y), values, empty_positions = solving_stack.pop()
        for x_1, y_1 in empty_positions:
            sudoku[x_1][y_1] = 0
        if len(values):
            sudoku[x][y] = values.pop()
            if len(values):
                solving_stack.append((x, y), values, empty_positions)

    solving_stack = []
    
    while (not is_a_valid_sudoku(sudoku)):
        fill_unique_positions(sudoku)
        if (is_a_valid_sudoku(sudoku)):
            return sudoku
        empty_positions = get_empty_squares(sudoku)
        if len(empty_positions) == 0:
            update_sudoku(sudoku, solving_stack)
            continue
        possible_values = map(lambda p: get_posible_values(p, sudoku),
                              empty_positions)
        (x, y), values = sorted(zip(empty_positions, possible_values), key=lambda x: len(x[1]))[0]
        if len(values) == 0:
            update_sudoku(sudoku, solving_stack)
            continue

        empty_positions.remove((x, y))
        sudoku[x][y] = values.pop()
        solving_stack.append(((x, y), values, empty_positions))

    return sudoku


with open('p096_sudoku.txt', 'r') as f:
    s = 0
    sudoku = []
    total = 0
    for line in f.readlines():
        if line[0] == 'G': continue
        sudoku.append(map(int, line.rstrip())) 
        s += 1
        if s == 9:
            sudoku = solve_sudoku(sudoku)
            v = int(''.join(map(str, sudoku[0][0:3])))
            total += v 
            for row in sudoku: print row
            print v
            sudoku = []
            s = 0
    print total

