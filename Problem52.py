from itertools import dropwhile, count

def generate_sorted_digits(n):
    return sorted(str(n))

def check_number(n):
    return generate_sorted_digits(n * 2) ==\
        generate_sorted_digits(n * 3) ==\
        generate_sorted_digits(n * 4) ==\
        generate_sorted_digits(n * 5) ==\
        generate_sorted_digits(n * 6)

print dropwhile(lambda x: not check_number(x), count(1)).next()
