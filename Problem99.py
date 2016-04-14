from math import log

max_square = -1
line_num = 0
with open('p099_base_exp.txt', 'r') as f:
    for num, line in enumerate(f.readlines(), start=1):
        n1, n2 = map(int, line.split(','))
        p = n2 * log(n1)
        if p > max_square:
            max_square = p
            line_num = num
    
print line_num
