#!/usr/bin/env python3

import sys

s = sys.stdin.read().rstrip()

counts = 0
i = 0
while i < len(s):
  if s[i] >= "A" and s[i] <= "Z":
    counts = counts + 1
  i = i + 1

print(counts)
