from itertools import combinations

coins = (1, 2, 5, 10, 20, 50, 100, 200)


def compute_choices(c, total=200):
    if len(c) == 1:
        if (total % c[0]) == 0: return 1
        else: return 0

    if total < 0: return 0
    if total == 0: return 1

    return compute_choices(c[:-1], total) + compute_choices(c, total-c[-1])

# Get all the possible combinations of coins
# that can make 200
#c = [sorted(comb) for i in range(len(coins))
#                  for comb in combinations(coins, i)
#                  if sum(comb) <= 200 and comb]

#print sum(map(compute_choices, c))
print compute_choices(coins)
