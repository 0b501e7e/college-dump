#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for word in lines:
  word = word.strip()
  if len(word) % 2 == 0:
    print("No middle character!")
  else:
    middle = word[len(word) // 2]
    print(middle)
