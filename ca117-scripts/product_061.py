#!/usr/bin/env python3

import sys

import math

nums = sys.stdin.readline()
num = [int(num) for num in nums.strip() if int(num) > 0]
res = 10

while res > 9:
  try:
    res = str(num[0] * num[1])
  except IndexError:
    print(str(num[0])
  res = res.strip()
  num = [int(n) for n in res if int(n) > 0]
  res = int(res)
  if res <= 9:
    break
print(res)
