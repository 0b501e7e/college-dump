#!/usr/bin/env python3

import sys

args = sys.argv[1:]

i = 0
while i < len(args):
  with open(args[i]) as f:
    lines = f.read()
  if len(lines) > 0:
    print(args[i])
  i = i + 1
