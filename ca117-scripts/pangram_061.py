#!/usr/bin/env python3

import sys

def isPangram(s):
  s = s.lower()
  s = set(s)
  alphabet = [c for c in s if ord(c) in range(ord("a"), ord("z") + 1)]
  if len(alphabet) == 26:
    return "pangram"
  else:
    alphamap = "abcdefghijklmnopqrstuvwxyz"
    missing = [c for c in alphamap if c not in alphabet]
    return f'missing {"".join(missing)}'

for line in sys.stdin:
  line = line.strip()
  print(isPangram(line))
