#!/usr/bin/env python3

import sys

n = 13

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

src = lower + upper

dst = lower[n:] + lower[:n] + upper[n:] + upper[:n]

i = 0
newdict = {}
while i < len(src):
  newdict[src[i]] = dst[i]
  i = i + 1


endline = ""

line = sys.stdin.read().strip()
i = 0
while i < len(line):
  if line[i] in newdict:
    endline += newdict[line[i]]
  else:
    endline += line[i]
  i = i + 1

print(endline)
