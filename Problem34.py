from math import factorial


def sfd(n):
    def get_digits(r):
        digits = []
        while (r > 9):
            digits.append(r % 10)
            r /= 10
        digits.append(r)
        return digits

    if sum(map(factorial, get_digits(n))) == n:
        return True

    return False

print sum(filter(sfd, xrange(3, 3000001)))
