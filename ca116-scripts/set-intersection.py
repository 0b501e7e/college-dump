#!/usr/bin/env python3

import sys

newdict = {}

with open("a.txt") as f:
  data = f.read()
with open("b.txt") as g:
  data2 = g.read()


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
    newdict[line] += 1
  elif line not in newdict:
    newdict[line] = 1
  i = i + 1

for line in newdict:
  if newdict[line] > 1:
    print("intersecting")
  else:
    print("disjoint")
