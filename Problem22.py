from string import ascii_uppercase

letters = dict(zip(ascii_uppercase, xrange(1, 27)))

with open("names.txt") as f:
    names = f.readline()
    names = map(lambda x: x.strip('"'), names.split(","))

    names = sorted(names)
    total = 0
    for pos, name in enumerate(names, start=1):
        total += sum(map(lambda x: letters[x], name)) * pos

    print total
