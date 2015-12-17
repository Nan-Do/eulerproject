from itertools import chain
sum(chain(xrange(0, 1000, 3), xrange(0, 1000, 5))) - sum(xrange(0, 1000, 15))
