#!/usr/bin/env python3

import sys

n = sys.argv[1]

s = sys.stdin.readlines()

i = 0
while i < len(s):
  tokens = s[i].strip()
  tokens = str(tokens)
  n = str(n)
  b = tokens.split(n)
  if b[-1] == "":
    i = i + 1
  else:
    print(tokens)
    i = i + 1
