def generate_next_number(n):
    return sum(map(lambda x: int(x) ** 2, str(n)))

total = 0
for x in xrange(1, 10000000):
    numbers = set()
    last = generate_next_number(x)
    while last != 89 and last != 1:
        numbers.add(last)
        last = generate_next_number(last)
    if last == 89:
        total += 1
print total
