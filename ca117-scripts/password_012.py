#!/usr/bin/env python3

import sys

digit = 0
lower = 0
upper = 0
ascii = 0
passwords = sys.stdin.readlines()

for line in passwords:
  line = line.strip()
  for char in line:
    if char.isdigit() is True:
      digit = 1
    elif char.islower() is True:
      lower = 1
    elif char.isupper() is True:
      upper = 1
    else:
      ascii = 1
  print(digit + lower + upper + ascii)
  digit = 0
  lower = 0
  upper = 0
  ascii = 0
