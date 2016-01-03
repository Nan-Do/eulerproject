from fractions import Fraction, gcd

# left = Fraction(1, 10)
# ref = Fraction(3, 7)
# 
# for x in xrange(4, 1000001):
#     for y in xrange(x+1, 1000001):
#         value = x / float(y)
#         if value < left:
#             break
#         if gcd(x, y) != 1:
#             continue
#         if value > left and value < ref:
#             left = Fraction(x, y)
#             print left
# 
#print left

x = 8 
y = 19
while y < 1000000:
    x += 3
    y += 7

print x - 3

