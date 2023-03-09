#!/usr/bin/env python3

import sys

fruits = {"apple": True,
          "pear": True,
          "orange": True,
          "banana": True,
          "cherry": True,
          }

word = sys.stdin.readline().rstrip()
a = []
while word != "":
  if word in fruits:
    a.append(word)
  word = sys.stdin.readline().rstrip()

i = 0
while i < len(a):
  print(a[i])
  i = i + 1
