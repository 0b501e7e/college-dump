#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for word in lines:
  word = word.strip()
  first = word[0].upper()
  middle = word[1:-1]
  end = word[-1].upper()
  if len(word) >= 2:
    print(first + middle + end)
