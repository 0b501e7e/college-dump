#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for word in lines:
  word = word.strip()
  slice = word[1:-1]
  if len(slice) > 0:
    print(slice)
