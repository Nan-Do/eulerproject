def is_palindrome(n):
    a = str(n)
    return a == ''.join(reversed(a))

print max(filter(lambda x: is_palindrome(x), (x * y
                                              for x in xrange(999, 1, -1)
                                              for y in xrange(999, 1, -1))))
