#!/usr/bin/env python3

s = input()

while s != "end":
  words = s.split()
  print(" ".join(words[5:]))
  s = input()
