#!/usr/bin/env python3

import sys

import string

def tagger(item):
  return item[1]

words = sys.stdin.read().split()

d = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for word in words:
  word = word.strip(string.punctuation + string.whitespace).lower()
  word = word.strip()
  for char in word:
    if char in d:
      d[char] += 1
for k, v in sorted(d.items(), key=tagger, reverse=True):
  leng = len(str(max(d.values())))
  print(f'{k:>1s} : {v:>{leng}d}')
