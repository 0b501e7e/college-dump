#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for line in lines:
    line = line.strip().split()
    line.sort()
    line = [int(x) for x in line]
    if len(line) >= 3:
        amtFree = len(line) // 3
        i = 1
        while i <= amtFree:
            line.pop(-3)
            i += 1
        print(sum(line))
    elif len(line) < 3:
        print(sum(line))
