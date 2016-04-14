Numerals = {'I' : 1,
            'IV': 4,
            'V' : 5,
            'IX': 9,
            'X' : 10,
            'XL': 40,
            'L' : 50,
            'XC': 90,
            'C' : 100,
            'CD': 400,
            'D' : 500,
            'CM': 900,
            'M' : 1000}

Values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
Romans = {1 : 'I',
          4 : 'IV',
          5 : 'V',
          9 : 'IX',
          10: 'X',
          40: 'XL',
          50: 'L',
          90: 'XC',
          100: 'C',
          400: 'CD',
          500: 'D',
          900: 'CM',
          1000: 'M'}
            
def roman_to_numeral(roman):
    numeral = 0
    while roman:
        if len(roman) >= 2 and roman[:2] in Numerals:
            numeral += Numerals[roman[:2]]
            roman = roman[2:]
            continue
        numeral += Numerals[roman[0]]
        roman = roman[1:]
    return numeral

def numeral_to_roman(numeral):
    roman = ''
    pos = 0
    while numeral > 0:
        while numeral >= Values[pos] :
            roman += Romans[Values[pos]]
            numeral -= Values[pos]
        pos += 1
    return roman

saved = 0
with open('p089_roman.txt') as f:
    for line in f.readlines():
        roman = line.strip()
        minimal_roman = numeral_to_roman(roman_to_numeral(roman))
        saved += len(roman) - len(minimal_roman)
print saved

#print roman_to_numeral('CCCLXXXXIX')
#print numeral_to_roman(49)
