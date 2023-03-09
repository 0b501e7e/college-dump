#!/usr/bin/env python3

import sys

fname = sys.argv[1]

message = sys.argv[2:]

i = 0

with open(fname, "w") as f:
  while i < len(message):
    f.write(message[i] + "\n")
    i = i + 1
