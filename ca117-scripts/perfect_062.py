#!/usr/bin/env python3

import sys

from math import sqrt

def sumFac(n):
  ans = 0
  res = [i for i in range(1, int(n)) if n % i == 0]
  return sum(res)

posint = sys.stdin.readlines()

for line in posint:
  line = int(line.strip())
  if int(line) == sumFac(line):
    print("True")
  else:
    print("False")
