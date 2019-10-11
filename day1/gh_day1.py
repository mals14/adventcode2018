# https://github.com/fogleman/AdventOfCode2018/blob/master/1.py

import fileinput

lines = list(fileinput.input('day1/input1_1.txt')) 
# link -> https://effbot.org/librarybook/fileinput.htm


def part1():
    return sum(map(int, lines))

def part2():
    f = 0
    seen = {f}
    while True:
        for line in lines:
            f += int(line)
            if f in seen:
                return f
            seen.add(f)

print(part1())
print(part2())