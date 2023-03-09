#!/usr/bin/env python3

import sys

import string

words = sys.stdin.read().split()

d = {}

for word in words:
  word = word.strip(string.punctuation + string.whitespace).lower()
  if word not in d:
    d[word] = 1
  else:
    d[word] += 1
for k, v in sorted(d.items()):
  if len(k) > 3 and v >= 3:
    print(f'{k:>9s}' + " : " + f'{v:>2d}')
