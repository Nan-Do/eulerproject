from itertools import count

max_value = 0
for x in xrange(2, 10000):
    for y in count(start=2):
        num = ''.join(map(str, map(lambda z: z*x, xrange(1, y))))
        if len(num) == 9 and len(set(num)) == 9 and '0' not in num:
            n = int(num)
            if n > max_value:
                max_value = n
                print x, n
        if len(num) > 9:
            break
print max_value
