#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for line in lines:
  line = line.strip()
  word, num = line.split()
  num = int(num)
  num = num % len(word)
  print(word[-num:] + word[:-num])
