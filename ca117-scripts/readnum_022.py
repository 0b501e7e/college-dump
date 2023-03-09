#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for line in lines:
  line = line.strip()
  if line < "0" or line > "9":
    print(f'{line} is not a number')
  else:
    print(f'Thank you for {line}')
    break
