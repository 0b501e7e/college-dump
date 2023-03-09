#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for line in lines:
  line = line.split()
  sub = line[0].lower()
  word = line[1].lower()
  print(sub in word)
