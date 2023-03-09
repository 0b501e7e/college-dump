#!/usr/bin/env python3

import sys
import string

lines = sys.stdin.readlines()

for line in lines:
  line = line.rstrip()
  line = line.translate(str.maketrans("", "", string.punctuation))
  line = line.replace(" ", "").lower()
  copy = line[::-1]
  if line == copy:
      print(True)
  else:
      print(False)
