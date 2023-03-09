#!/usr/bin/env python3

import sys

nums = sys.stdin.readlines()

for num in nums:
  print(f'Primes: {[x for x in range(2, int(num)) if all(x % y for y in range(2, x))]}')
