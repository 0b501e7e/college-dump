#!/usr/bin/env python3

import sys

def contains(left, right):
  for c in left:
    if c in right:
      right = right.replace(c, "", 1)
    else:
      return False
  return True

for line in sys.stdin:
  [left, right] = line.strip().lower().split()
  print(contains(left, right))
