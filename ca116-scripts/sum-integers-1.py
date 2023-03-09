#!/usr/bin/env python3

import sys

file = sys.stdin.readline()

file = file.strip()

total = 0

while file != "":
  total = total + int(file)
  file = sys.stdin.readline()
  file = file.strip()

print(total)
