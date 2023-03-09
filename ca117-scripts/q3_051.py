#!/usr/bin/env python3

import sys

def helper(c):
  if c.isupper():
    return c
  return "0"

lines = sys.stdin.readlines()

for line in lines:
  line = line.strip()
  uppers = "".join([helper(c) for c in line])
  ul = uppers.split("0")
  print(max(ul, key=len))
