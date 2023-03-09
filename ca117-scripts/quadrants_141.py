#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for line in lines:
    x, y = line.strip().split()
    x, y = int(x), int(y)
    if x > 0 and y > 0:
        print("1")
    elif x > 0 and y < 0:
        print("2")
    elif x < 0 and y > 0:
        print("4")
    elif x < 0 and y < 0:
        print("3")
