from collections import namedtuple
from operator import itemgetter

Card = namedtuple('Card', ['rank', 'suit'])

def create_card(card):
    if len(card) == 2:
        rank, suit = card
    else:
        rank = card[0:2]
        suit = card[2]

    if rank == 'T':
        rank = 10
    elif rank == 'J':
        rank = 11
    elif rank == 'Q':
        rank = 12
    elif rank == 'K':
        rank = 13
    elif rank == 'A':
        rank = 14
    else:
        rank = int(rank)

    return Card(rank, suit)

def create_hand(hand):
    return sorted(map(create_card, hand.split(' ')),
                  key=itemgetter(0))

def generate_game(hand):
    def group_ranks(ranks):
        s = set(ranks)
        res = []
        for v in s:
            res.append(filter(lambda x: x == v, ranks))
        return res

    def check_straight(ranks):
        for i in xrange(len(ranks) - 1):
            if (ranks[i + 1] - ranks[i]) != 1:
                return False
        return True

    def check_flush(suits):
        return len(set(suits)) == 1

    def check_straight_flush(ranks, suits):
        return check_straight(ranks) and\
            check_flush(suits)

    def check_royal_straight(ranks, suits):
        return ranks[0] == 10 and\
            check_straight_flush(ranks, suits)

    def create_game(groups, ranks, suits):
        groups = sorted(groups, key=len)
        g = map(len, groups)

        # Check for equal card games (pair, poker, full, ...)
        if g[-1] == 2 and len(g) == 4:
            return 2, groups[-1][0], ranks
        elif g == [1, 2, 2]:
            return 3, max(groups[1][0], groups[2][0]), ranks
        elif g == [1, 1, 3]:
            return 4, groups[-1][0], ranks
        elif g == [2, 3]:
            return 7, groups[1][0], ranks
        elif g == [1, 4]:
            return 8, groups[1][0], ranks

        # Check for straights
        elif check_royal_straight(ranks, suits):
            return 10, ranks[-1], ranks
        elif check_straight_flush(ranks, suits):
            return 9, ranks[-1], ranks
        elif check_straight(ranks):
            return 5, ranks[-1], ranks

        # Check for flush
        elif check_flush(suits):
            return 6, ranks[-1], ranks

        # Highest card
        else:
            return 1, ranks[-1], ranks

        return None, None

    ranks = [x.rank for x in hand]
    suits = [x.suit for x in hand]
    groups = group_ranks(ranks)

    return create_game(groups, ranks, suits)

def compare_games(g1, g2):
    hand_score1, high_card1, ranks1 = g1
    hand_score2, high_card2, ranks2 = g2

    if hand_score1 > hand_score2:
        return 1
    elif hand_score2 > hand_score1:
        return -1

    if high_card1 > high_card2:
        return 1
    elif high_card2 > high_card1:
        return -1

    for i, j in zip(ranks1[::-1], ranks2[::-1]):
        if i > j:
            return 1
        if j > i:
            return -1

    return 0

a = generate_game(create_hand('10S JS QS KS AS'))
b = generate_game(create_hand('10S 2C 2S 2J AS'))
#print compare_games(b, a)

f = open('p054_poker.txt')
count = 0
for line in f.readlines():
    g1 = generate_game(create_hand(line[:14]))
    g2 = generate_game(create_hand(line[15:-1]))

#     if g1[0] == g2[0]:
#         print line[:14], g1, "\t", line[15:-1], g2, compare_games(g1, g2)

    if compare_games(g1, g2) >= 0:
        count += 1

print count
