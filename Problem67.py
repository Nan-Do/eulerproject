def read_pyramid():
    pyramid = []
    with open('p067_triangle.txt', 'r') as f:
        for line in f.readlines():
            pyramid.append(map(int, line.split(' ')))
    return pyramid


rows = reversed(read_pyramid())
pivot_row = rows.next()
for row in rows:
    temp_row = []
    for position, element in enumerate(row):
        a = element + pivot_row[position]
        b = element + pivot_row[position+1]
        temp_row.append(max(a, b))
    pivot_row = temp_row

print pivot_row[0]
