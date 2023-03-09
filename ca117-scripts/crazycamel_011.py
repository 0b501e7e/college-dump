#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for line in lines:
  line = line.strip()
  line = line[::-1]
  line = line.title()
  line = line[::-1]
  print(line)
