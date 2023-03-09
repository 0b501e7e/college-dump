#!/usr/bin/env python3

import sys
newdict = {}
s = sys.stdin.readline().rstrip()
while s != "":
  if s not in newdict:
    newdict[s] = 1
  elif s in newdict:
    newdict[s] = 2
  s = sys.stdin.readline().rstrip()
for word in newdict:
  if newdict[word] == 1:
    print(word)
