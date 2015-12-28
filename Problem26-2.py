from itertools import tee, islice

def make_division(n):
    x = 10
    while x < n:
        x *= 10
    while 1:
        r, x = divmod(x, n)
        yield r
        if x == 0:
            return
        while x < n:
            x *= 10
 
def cycle_hare(n):
    def move(n, steps=1):
        for x in xrange(1, steps):
            n.next()
        return n.next()

    t, h = tee(n)
    tortoise = move(t) 
    hare = move(h, 2) 
    
    while tortoise != hare:
        tortoise = move(t)
        hare = move(h, 2)

    mu = 0
    t = tee(n, 1)[0]
    while tortoise != hare:
        tortoise = move(t)
        hare = move(h)
        mu += 1
       
    lam = 1
    hare = move(t)
    while tortoise != hare:
        hare = move(t)
        lam += 1

    return lam


def cycle_length(x, rr_size=4):
    def fall_into_cycle(n):
        def move(n, steps=1):
            try:
                for x in xrange(1, steps):
                    n.next()
                return n.next()
            except StopIteration:
                return 0

        t, h = tee(n)
        tortoise = move(t) 
        hare = move(h, 2) 
        
        while tortoise != hare:
            tortoise = move(t)
            hare = move(h, 2)

        return t

    value_generator = fall_into_cycle(make_division(x))
    # Fill the comparison buffer
    initial_values = list(islice(value_generator, rr_size))
    if len(initial_values) != rr_size:
        return -1
    comparation_sequence = list(islice(value_generator, rr_size))
    lenght = rr_size
    while lenght < 1000:
        if initial_values == comparation_sequence:
            return lenght
        try:
            next_value = next(value_generator)
            comparation_sequence.pop(0)
            comparation_sequence.append(next_value)
            lenght += 1
        except StopIteration:
            return -1
    return -1 


m = v = 0
for x in xrange(2, 1001):
    value = cycle_length(x)
    if value > v:
        v = value
        m = x
    #print x, value
    
print m, v
