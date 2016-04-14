from itertools import count
from sys import exit
from math import ceil

increment = 0.00000000001
value = 0.7071067811541

#for x in count(start=1):
for x in count(start=122410000000):
    if x % 10000000 == 0:
        print x
    a = int(ceil(x * value))
    c = x * (x - 1) 
    total = 0
    while True:
        total += 1
        v = 2 * (a * (a-1))
        #print (pow(a, 2) - a)/float(c)
        if v == c:
            print a, x-a, x
            exit(0)
            #break
        elif v > c:
            break
        a += 1; 
    if total > 200:
       value += increment 
       print 'XXXXXXXXX'


