#!/usr/bin/env python3

import sys

arg = sys.argv[1]

with open(arg) as f:
  lines = f.readlines()

i = 0

count = 0

while i < len(lines):
  count = count + int(lines[i])
  i = i + 1

print(count)
