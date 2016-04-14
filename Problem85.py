from itertools import count

# The solvig algorithim goes as follows
# At every round we compute the number of squares of a certain size
# For example (1, 1) which is n*m. Every time we increase the
# size of one of the sides we decrease it from the bigger side.
# For example the number of squares of size (2, 2) on a n*m square 
# would be (n - 1) * (m -1) as we increased every side by one.
# This probably can be extracted in a general function by unrolling the sums
# and generating a general formula. Taht would lead to a constant cost instead
# of a quadratic one (in the worst case) but n*m is good enough for the proposed 
# problem so no further analysis is required.
def compute_squares(n, m):
    total = 0
    for x in xrange(n):
        for y in xrange(m):
            total += (n - x) * (m - y)
    return total

closest = 0
values = ()
for x in count(start=1):
    for y in count(start=1):
        squares = compute_squares(x, y)
        if squares < 2000000 and squares > closest:
            values = (x, y)
            closest = squares
        if squares > 2000000:
            break
    if x > 100: break
print values[0] * values[1] 
