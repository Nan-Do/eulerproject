import random

dice = [1,2,3,4]
plays = 1000000
totals = [0] * 40
square = 0
CC = {2, 17, 33}
CH = {7, 22, 36}
CC_CARDS = range(0, 16)
CH_CARDS = range(0, 16)
random.shuffle(CC_CARDS)
random.shuffle(CH_CARDS)
doubles = 0

def cc_movemement(square):
    card = CC_CARDS.pop(0)
    CC_CARDS.append(card)

    if card == 0 or card == 10:
        square = card

    return square

def ch_movement(square):
    card = CH_CARDS.pop(0)
    CH_CARDS.append(card)

    if card == 0:
        square = 0
    elif card == 1:
        square = 10
    elif card == 2:
        square = 11
    elif card == 3:
        square = 24
    elif card == 4:
        square = 39
    elif card == 5:
        square = 5
    elif card == 6 or card == 7:
        if square == 7:
            square = 15
        elif square == 22:
            square = 25
        else:
            square = 5
    elif card == 8:
        if square == 7 or square == 36:
            square = 12
        else:
            square = 28
    elif card == 9:
        square -= 3

    return square

for _ in xrange(plays):
    dice_1 = random.choice(dice)
    dice_2 = random.choice(dice)
    square += dice_1 + dice_2
    square %= 40
    
    if dice_1 == dice_2:
        doubles += 1
        if doubles == 3:
            doubles = 0
            square = 10
    else:
        doubles = 0
    
    if square in CC:
        square = cc_movemement(square)
    elif square in CH:
        square = ch_movement(square)
        if square == 33:
            square = cc_movemement(square)
    elif square == 30:
        square = 10

    totals[square] +=1

#print sum(map(lambda x: (x / float(plays)) * 100, totals)) / 40.0
# Compute probabilities
totals = map(lambda x: (x / float(plays)) * 100, totals)
totals = list(enumerate(totals))
print sorted(totals, key=lambda x: x[1], reverse=True)
