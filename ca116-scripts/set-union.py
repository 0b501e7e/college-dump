#!/usr/bin/env python3

import sys

newdict = {}

with open("a.txt") as f:
  data = f.read()
with open("b.txt") as g:
  data2 = g.read()

lines = data + data2

lines = lines.rstrip().split()

i = 0
while i < len(lines):
  line = lines[i]
  if line not in newdict:
    newdict[line] = 1
    print(line)
  i = i + 1
