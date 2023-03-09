#!/usr/bin/env python3

import sys

newdict = {}

with open("a.txt") as f:
  data = f.read()
with open("b.txt") as g:
  data2 = g.read()


intersect = False

data = data.rstrip().split()
i = 0
while i < len(data):
  line = data[i]
  if line not in newdict:
    newdict[line] = 1
  elif line in newdict:
    newdict[line] += 1
  i = i + 1

data2 = data2.rstrip().split()
i = 0
while i < len(data2):
  line = data2[i]
  if line in newdict:
    intersect = True
  i = i + 1

if intersect is True:
  print("intersecting")
else:
  print("disjoint")
