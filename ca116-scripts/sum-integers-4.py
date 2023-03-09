#!/usr/bin/env python3

import sys

args = sys.argv[1:]

i = 0

total = 0

while i < len(args):
  nums = args[i]
  while nums != "":
    file = nums.readline()
    file = file.strip()
    total = total + int(file)
  i = i + 1
