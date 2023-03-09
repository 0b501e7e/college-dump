#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for line in lines:
  line = line.strip()
  line = list(line)
  lens = len(line)
  i = 1
  while i < lens:
    line[i - 1], line[i] = line[i], line[i - 1]
    i += 2
  print("".join(line))
