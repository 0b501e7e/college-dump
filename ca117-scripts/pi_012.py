#!/usr/bin/env python3

import math
import sys

placeval = sys.stdin.readlines()

pi = math.pi

for num in placeval:
  num = int(num.strip())
  print(f'{pi:.{num}f}')
