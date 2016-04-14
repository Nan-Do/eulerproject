from math import sqrt 

def get_square_of_a_perfect_square(n):
    last_digit = n % 10
    if last_digit == 2 or last_digit == 3 or last_digit == 7 or last_digit == 8:
        return None

    x = n // 2
    seen = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in seen: return None
        seen.add(x)
    return x

def get_h(a, b):
    return get_square_of_a_perfect_square(pow(a, 2) - pow(b, 2))

total = 0
for x in xrange(3, 1000000000, 2):
    p_1 = (x * 2) + (x - 1)
    if p_1 > 1000000000:
        break
    if get_h(x, (x-1) // 2):
        print x, x, x-1
        total += p_1
    
    p_2 = (x * 2) + (x + 1)
    if p_2 > 1000000000:
        break
    if get_h(x, (x+1) // 2):
        print x, x, x+1
        total += p_2
print total
