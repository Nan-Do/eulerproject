def up_to_ten(n):
    if n == 1: return "one"
    if n == 2: return "two"
    if n == 3: return "three"
    if n == 4: return "four"
    if n == 5: return "five"
    if n == 6: return "six"
    if n == 7: return "seven"
    if n == 8: return "eight"
    if n == 9: return "nine"
    if n == 10: return "ten"


def ten_to_twenty(n):
    if n == 11: return "eleven"
    if n == 12: return "twelve"
    if n == 13: return "thirteen"
    if n == 14: return "fourteen"
    if n == 15: return "fifteen"
    if n == 16: return "sixteen"
    if n == 17: return "seventeen"
    if n == 18: return "eighteen"
    if n == 19: return "nineteen"


def dozens(n):
    if n == 2: return "twenty"
    if n == 3: return "thirty"
    if n == 4: return "forty"
    if n == 5: return "fifty"
    if n == 6: return "sixty"
    if n == 7: return "seventy"
    if n == 8: return "eighty"
    if n == 9: return "ninety"


def number_to_word(n):
    result = ""
    if n == 1000: return "one thousand"
    if n >= 100:
        result += up_to_ten(n / 100) + " hundred"
        if (n % 100) != 0: result += " and "
        n = (n % 100)

    if (n ==0): return result

    if n >= 20:
        result += dozens(n / 10)
        if (n % 10) != 0:
            result += "-" + up_to_ten(n % 10)
        return result
    if n > 10:
        if result:
            return result + ten_to_twenty(n)
        return ten_to_twenty(n)

    if result:
        return result + up_to_ten(n)
    return up_to_ten(n)


def count(s):
    return len(s.strip("- "))


#print sum(map(count, map(number_to_word, xrange(1, 1000)))) + len("one thousand")
print sum(len(number_to_word(x).translate(None, " -")) for x in xrange(1, 1001))
