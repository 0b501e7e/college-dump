#!/usr/bin/env python3

import sys

nums = sys.stdin.readlines()

for num in nums:
  num = num.strip().split()
  bin = num[0]
  base = num[1]
  bin = bin[::-1]
  bin = str(bin)
  i = 0
  answer = 0
  while i < len(bin):
    answer += (int(bin[i]) * (int(base) ** i))
    i += 1
  print(answer)
