from datetime import date

count = 0
for year in xrange(1901, 2001):
    for month in xrange(1, 13):
        if date(year, month, 1).weekday() == 6:
            print str(year) + "/" + str(month)
            count += 1

print count
