#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for num in lines:
  values = list(range(1, (int(num) + 1)))
  print(f'Multiples of 3 replaced: {["X" if not i % 3 else i for i in values]}')
