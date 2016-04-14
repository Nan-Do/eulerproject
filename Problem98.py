from itertools import combinations, permutations

def square_anagram(w1, w2, squares=set(map(lambda x: x * x,
                                           xrange(1, 1000)))):
    def compute_number(w, nums):
        n = map(lambda x: nums[x], w)
        if n[0] == 0: return -1
        total = 0
        for p, v in enumerate(n[::-1]):
            total += v * (10 ** p)
        return total

    s = set(w1)
    for n in combinations(xrange(10), len(s)):
        for p in permutations(n):
            nums = dict(zip(s, p))
            n1 = compute_number(w1, nums)
            n2 = compute_number(w2, nums)
            if n1 in squares and n2 in squares:
                return max(n1, n2)
    return -1

        

words = []
max_square = -1
with open('p098_words.txt', 'r') as f:
    words = map(lambda x: x[1:-1], f.readline().split(','))

for p, w1 in enumerate(words, start=1):
    for w2 in words[p:]:
        if len(w1) == len(w2) and sorted(w1) == sorted(w2) and not w1 == w2[::-1]:
            v = square_anagram(w1, w2)
            if v > max_square: max_square = v
print max_square
