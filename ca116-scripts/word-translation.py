#!/usr/bin/env python3

import sys
newdict = {}
a = []
i = 0
with open("translation.txt") as f:
  lines = f.readlines()
while i < len(lines):
  line = lines[i]
  line = line.split()
  newdict[line[0]] = line[1]
  i = i + 1

input = sys.stdin.readline().rstrip()
while input != "":
  if input in newdict:
    a.append(newdict[input])
  input = sys.stdin.readline().rstrip()

j = 0
while j < len(a):
  print(a[j])
  j = j + 1
