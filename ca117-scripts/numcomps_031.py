#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for num in lines:
  num = num.strip()
  lst = list(range(1, (int(num) + 1)))
  print(f'Multiples of 3: {[i for i in lst if not i % 3]}')
  print(f'Multiples of 3 squared: {[i ** 2 for i in lst if not i % 3]}')
  print(f'Multiples of 4 doubled: {[i * 2 for i in lst if not i % 4]}')
  print(f'Multiples of 3 or 4: {[i for i in lst if not i % 3 or not i % 4]}')
  print(f'Multiples of 3 and 4: {[i for i in lst if not i % 3 and not i % 4]}')
