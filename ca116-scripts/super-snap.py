#!/usr/bin/env python3

import sys
newdict = {}
a = []
b = []
line = sys.stdin.readline().rstrip()
while line != "":
  if line not in newdict:
    newdict[line] = 1
    a.append(line)
  elif line in newdict:
    newdict[line] = newdict[line] + 1
    b.append(line)
  line = sys.stdin.readline().rstrip()

if len(b) > 0:
  print("snap:" + " " + b[0])
