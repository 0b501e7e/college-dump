#!/usr/bin/env python3

import sys

args = sys.argv[1:]


i = 0

k = 0

m = 0

count = 0

while i < len(args):
  fname = args[i]
  with open(fname) as f:
    lines = f.readlines()

  while k < len(lines):
    nums = lines[k].split()
  while m < len(nums):
    count = count + int(nums[m])
    m = m + 1
  i = i + 1
  k = 0
  m = 0

print(count)
