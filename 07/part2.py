import sys
from collections import Counter

hands = []

for line in sys.stdin.readlines():
    hand, bid = line.strip().split(' ')
    bid = int(bid)
    hands.append((hand, bid))

cardvals = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'J': 0,
    'T': 9,
}
for i in range(2, 10):
    cardvals[str(i)] = i - 1

def cardval(card):
    return cardvals[card]

def strength(arg):
    hand, _ = arg
    c = Counter(hand)
    if 'J' in c and len(c) > 1:
        ordered = sorted([i for i in c.items() if i[0] != 'J'],
                         key=lambda i: i[1], reverse=True)
        ordered[0] = (ordered[0][0], ordered[0][1] + c['J'])
        c = dict(ordered)
    counts = set(c.values())
    count_counts = Counter(c.values())
    if max(counts) == 5:
        type = 6
    elif max(counts) == 4:
        type = 5 
    elif 3 in counts and 2 in counts:
        type = 4
    elif max(counts) == 3:
        type = 3
    elif max(counts) == 2 and count_counts[2] == 2:
        type = 2
    elif max(counts) == 2:
        type = 1
    else:
        type = 0
    score = type << 20
    shift = 16
    for v in map(cardval, hand):
        score |= v << shift
        shift -= 4
    return score

ranks = sorted(hands, key=strength)
tot = 0
for i, (_, bid) in enumerate(ranks):
    tot += bid * (i + 1)
print(tot)
