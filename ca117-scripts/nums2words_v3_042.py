#!/usr/bin/env python3

import sys

file = sys.argv[1]

with open(file) as f:
  map = f.readlines()

d = {}

e = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten"}

for line in map:
  line = line.split()
  d[line[0]] = line[1]

input = sys.stdin.readlines()

for line in input:
  res = [e[num] for num in line.split()]
  end = [d[word] for word in res]
  print(" ".join(end))
