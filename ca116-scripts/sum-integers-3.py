#!/usr/bin/env python3

import sys

args = sys.argv[1:]


i = 0

count = 0

while i < len(args):
  with open(args[i]) as f:
    lines = f.readlines()
  j = 0
  while j < len(lines):
    lines[j] = lines[j].rstrip()
    count = count + int(lines[j])
    j = j + 1
  i = i + 1

print(count)
