#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

a = []

for line in lines:
    line = line.split()
    for word in line:
        word = word.capitalize()
        a.append(word)
    print(" ".join(a))
    a = []
