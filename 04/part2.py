import sys
import re

cards = {}
for line in sys.stdin.readlines():
    card, play = line.split(':')
    card = int(re.split('\s+', card)[1])
    winning, my = play.split('|')
    winning = set(map(int, re.split('\s+', winning.strip())))
    my = set(map(int, re.split('\s+', my.strip())))
    l = len(winning & my)
    cards[card] = l

def v(card):
    tot = 1
    for i in range(card + 1, card + cards[card] + 1):
        tot += v(i)
    return tot

tot = 0
for card in cards.keys():
    tot += v(card)
print(tot)
