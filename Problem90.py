from itertools import combinations

squares = [(0, 1),
           (0, 4),
           (0, 9),
           (1, 6),
           (2, 5),
           (3, 6),
           (4, 9),
           (6, 4),
           (8, 1)]


def check_value_dice(value, dice):
    if value == 6 or value == 9:
        return (6 in dice or 9 in dice)
    else:
        return value in dice

total = 0
for d1 in combinations(xrange(0, 10), 6):
    extended_sets = set()
    for d2 in combinations(xrange(0, 10), 6):
        all_squares = True
        for v1, v2 in squares:
            if not ((check_value_dice(v1, d1) and check_value_dice(v2, d2)) or\
                    (check_value_dice(v2, d1) and check_value_dice(v1, d2))):
                all_squares = False
                break
        if all_squares:
            extended_sets.add(d2)
    total += len(extended_sets)
print total / 2

