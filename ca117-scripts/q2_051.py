#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

def is_evil(s):
  return [c for c in s if c in "evil"] == list("evil")

word_list = [line.strip() for line in lines]

evil_list = [w for w in word_list if is_evil(w.lower())]

for w in evil_list:
  print(w)
