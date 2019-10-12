# from https://github.com/fogleman/AdventOfCode2018/blob/master/2.py

from collections import Counter
# to understand Counter
# https://docs.python.org/3.7/library/collections.html#collections.Counter

import fileinput

input_file = '2.txt'

lines = [x.strip() for x in fileinput.input(input_file)]

def part1():
    has2 = 0
    has3 = 0
    for line in lines:
        c = Counter(line).values()
        has2 += 2 in c
        has3 += 3 in c
    return has2 * has3

def part2():
    for line1 in lines:
        for line2 in lines:
            x = ''.join(a for a, b in zip(line1, line2) if a == b)
            if len(x) == len(line1) - 1:
                return x

print(part1())
print(part2())
