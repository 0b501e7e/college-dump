#!/usr/bin/env python3

import sys

file = sys.argv[1]

def calcalc(file):
  d = {}
  with open(file) as f:
    lines = f.readlines()
  i = 0
  for line in lines:
    while i < len(line) and line[i] < "0" or line[i] > "9":
      i += 1
    if i < len(line):
      name, value = line[:i], line[i:]
    d[name] = value
  return d

d = calcalc(file)
nd = {}

for line in sys.stdin:
  line = line.strip().split(",", 1)
  name, foods = line[0], line[1].split(",")
  calvals = [d[num] for num in foods if d[num] in d]
  sum = sum(calvals)
  nd[name] = sum

for (k, v) in sorted(nd.items()):
  print(f'{k} : {v}')
