#!/usr/bin/env python3

message = "Hello world.\n"

import sys

fname = sys.argv[1]

with open(fname, "w") as f:
  f.write(message)
