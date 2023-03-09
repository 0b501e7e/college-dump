#!/usr/bin/env python3

import sys

arg = sys.argv[1]

with open(arg) as f:
  lines = f.readlines()

i = 0

k = 0

count = 0

while i < len(lines):
  nums = lines[i].split()
  while k < len(nums):
    count = count + int(nums[k])
    k = k + 1
  i = i + 1
  k = 0
print(count)
