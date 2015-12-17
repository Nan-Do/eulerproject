a = "".join(map(str, xrange(1, 500000)))

print int(a[1-1]) * int(a[10-1]) * int(a[100-1]) * int(a[1000-1]) *\
    int(a[10000-1]) * int(a[100000-1]) * int(a[1000000-1])
