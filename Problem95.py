def get_divisors_sum_number(n):
    divisors = [1]
    start=2
    increment=1
    if n % 2 != 0:
        start = 3
        increment = 2
    for x in xrange(start, (n//2) + 1,  increment):
        if n % x == 0:
            divisors.append(x)
    return sum(divisors) 

max_chain = set()
for x in xrange(1, 1000001):
    valid_chain = False
    chain = set()
    current = x
    while True:
        current = get_divisors_sum_number(current)
        if current in chain or current > 1000000:
            break
        chain.add(current)
        if current == x:
            valid_chain = True
            break
    if valid_chain and len(chain) > len(max_chain):
        max_chain = chain
        print sorted(max_chain)
