#!/usr/bin/env python3

import sys

a = sys.stdin.readlines()

i = 0

while i < len(a):
  p = i
  j = i + 1
  while j < len(a):
    word1 = a[p].split()
    word2 = a[j].split()
    if word2[1] < word1[1]:
      p = j
    elif word2[1] == word1[1]:
      if word2[0] < word1[0]:
        p = j
    j = j + 1
  tmp = a[p]
  a[p] = a[i]
  a[i] = tmp
  i = i + 1

i = 0
while i < len(a):
  print((a[i]).strip())
  i = i + 1
