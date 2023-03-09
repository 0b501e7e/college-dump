#!/usr/bin/env python3

import sys

args = sys.argv[1]

s = input()

while s != "end":
  i = 0
  found = False
  while i < len(s) and found is False:
    if s[i:i + len(args)] == args and i < len(s):
      print(s)
      found = True
    i = i + 1
  s = input()
