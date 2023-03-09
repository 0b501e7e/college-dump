#!/usr/bin/env python3

import sys

poem = sys.stdin.readlines()

longline = 0

for line in poem:
  line = line.rstrip()
  if len(line) > longline:
    longline = len(line)

for line in poem:
  line = line.rstrip()
  print(f'{line:^{longline}s}')
