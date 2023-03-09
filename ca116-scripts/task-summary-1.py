#!/usr/bin/env python3

import sys

a = []
newdict = {}

s = sys.stdin.readline().strip()
i = 0
while s != "":
  a.append(s)
  line = a[i]
  j = 0
  while line[j] != ".":
    j = j + 1
  file = line[:j + 3]
  answer = line[j + 4:]
  if file not in newdict and answer == "incorrect":
    newdict[file] = False
  elif file not in newdict and answer == "correct":
    newdict[file] = True
  elif file in newdict and answer == "incorrect":
    newdict[file] = False
  elif file in newdict and answer == "correct":
    newdict[file] = True
  s = sys.stdin.readline().strip()
  i = i + 1

for key in newdict:
  if newdict[key] is True:
    print(key)
