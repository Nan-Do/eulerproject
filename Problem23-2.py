def divisors(n):
    return filter(lambda x: (n % x == 0), xrange(2, (n/2) + 1))

abundants = set()
for n in xrange(2, 28124):
    if sum(divisors(n)) > n:
        abundants.add(n)

print len(abundants)

nums = set(x + y for x in abundants
                 for y in abundants)
print len(nums)

non_abundants = []
for x in xrange(1, 28124):
    if x not in nums:
        non_abundants.append(x)

print len(non_abundants), sum(non_abundants)
