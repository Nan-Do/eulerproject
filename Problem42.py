def generate_triangle_numbers_set(n):
    ans = set()
    for x in xrange(1, n+1):
        ans.add((x * (x+1)) / 2)
    return ans

def convert_word(word):
    return sum(map(lambda x: ord(x) - 64, word))

tn = generate_triangle_numbers_set(2000)

f = open('p042_words.txt')
count = 0
for word in f.readline().split(','):
    word = word[1:-1]
    if convert_word(word) in tn:
        count += 1

f.close()
print count
