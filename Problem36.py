def to_binary(n):
    res = ""
    while (n > 0):
        res = str(n % 2) + res
        n /= 2
    if n: res += str(n)
    return  res

def palindrome(n):
    return n == n[::-1]

print sum(filter(lambda x: palindrome(str(x)) and palindrome(to_binary(x)),
                 xrange(1, 1000001)))
