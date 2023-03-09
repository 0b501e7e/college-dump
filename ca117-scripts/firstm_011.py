#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for line in lines:
  pos = line.find("m")
  if pos == -1 and line[pos] != "m":
      print(line.rstrip())
  else:
      answer = line[:pos] + line[pos].upper() + line[pos + 1:]
      print(answer.rstrip())
