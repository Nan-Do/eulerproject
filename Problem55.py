def reverse(num):
    return int(str(num)[::-1])

def is_palindrome(num):
    a = str(num)
    return a == a[::-1]

count = 0
for i in xrange(10000):
    number = i
    palindrome_detected = False
    for _ in xrange(50):
        res = number + reverse(number)
        if is_palindrome(res):
            palindrome_detected = True
            break
        number = res
    if (palindrome_detected):
        continue
#    print i
    count += 1

print count
