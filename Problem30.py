def sum_powers(n):
    def get_digits(r):
        digits = []
        while (r > 9):
            digits.append(r%10)
            r /= 10
        digits.append(r)
        return digits

    return sum(map(lambda x: x**5, get_digits(n)))

answers = []
for x in xrange(10, 500000):
    if x == sum_powers(x):
        answers.append(x)

print sum(answers)
