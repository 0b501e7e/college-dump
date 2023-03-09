#!/usr/bin/env python3

s = input()

while s != "end":
  words = s.split()
  if int(words[2]) > 1:
    print(" ".join(words))
  s = input()
