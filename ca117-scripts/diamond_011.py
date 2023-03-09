#!/usr/bin/env python3

import sys

nums = sys.stdin.readlines()
for lines in nums:
  s = "* "
  i = 0
  j = 1
  a = []
  num = int(lines)
  while i < (num):
    triangle = (" " * (num - 1 - i) + s * j)
    print(triangle.rstrip())
    a.append(triangle)
    i += 1
    j += 1
  a = a[::-1]
  a = a[1:]
  for line in a:
    print(line.rstrip())
