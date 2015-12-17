from itertools import count

max_value = 0
for x in count(start=2):
    if len(str(x)) > 9: break
    for y in count(start=2):
        num = ''.join(map(str, map(lambda z: z*x, xrange(2, y))))
        if len(num) == 9:
            n = int(num)
            if len(set(num)) == 9\
                    and n > max_value:
                print n
                max_value = n
        if len(num) > 9:
            break
