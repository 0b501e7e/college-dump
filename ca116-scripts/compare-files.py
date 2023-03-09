#!/usr/bin/env python3

import sys

file1 = sys.argv[1]

file2 = sys.argv[2]

with open(file1) as f:
  a = f.readlines()

with open(file2) as g:
 b = g.readlines()

i = 0
j = 0
count = 0
while i < len(a) and j < len(b):
  line = a[i]
  line2 = b[i]
  while line[j] == line2[j]:
    j = j + 1
    if a[j] == "\n" and b[j] == "\n":
      count = count + 1
    if line[j] != line2[j]:
      print(count, i)
  i = i + 1
