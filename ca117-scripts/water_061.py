#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

amount = int(lines[0])

bucketlitres = lines[1].split()

count = 0

for num in bucketlitres:
  num = int(num)
  if amount > num:
    amount = amount - num
    count += 1
  else:
    break

print(count)
