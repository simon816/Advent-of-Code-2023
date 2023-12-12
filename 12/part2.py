import sys
import itertools
import re
import functools

pat = re.compile('\.+')

samples = []
for line in sys.stdin.readlines():
    springs, counts = line.strip().split(' ')
    counts = tuple(map(int, counts.split(',')))
    springs = ((springs + '?') * 5)[:-1]
    counts = counts * 5
    samples.append((springs, counts))

@functools.lru_cache(maxsize=None)
def count_matches(state):
    springs, counts = state
    counts = list(counts)
    springs = springs.lstrip('.')
    #print(repr(springs), counts, parent)
    while True:
        nstart = 0
        while springs.startswith('#'):
            springs = springs[1:]
            nstart += 1

        if nstart > 0:
            if len(counts) == 0:
                return 0
            count = counts.pop(0)
            while count > nstart and len(springs) > 0 and springs[0] in '?#':
                springs = springs[1:]
                nstart += 1
            if count != nstart:
                # Haven't reached the count, or consumed too many
                return 0             
            else:
                if len(springs):
                    if springs[0] == '?':
                        # consume ? as .
                        springs = springs[1:]
                    elif springs[0] != '.':
                        # no gap therefore no match
                        return 0
            springs = springs.lstrip('.')
        else:
            break

    if len(springs) == 0:
        if len(counts) == 0:
            #print("Valid")
            return 1
        return 0

    assert springs.startswith('?'), springs
    #print("  ->", springs[1:], tuple(counts))
    # Consume ? as .
    matches = count_matches((springs[1:], tuple(counts)))
    # Consume ? as #
    if len(counts) > 0:
        count = counts.pop(0)
        while count > 0 and len(springs) > 0 and springs[0] in '#?':
            count -= 1
            springs = springs[1:]
        if count == 0:
            if len(springs) == 0 or springs[0] != '#':
                # Force consume ? as .
                if len(springs) > 0 and springs[0] == '?':
                    springs = springs[1:]
                matches += count_matches((springs, tuple(counts)))
                #print("  ->", springs, tuple(counts))
    return matches

tot = 0
for sample in samples:
    tot += count_matches(sample)

print(tot)
