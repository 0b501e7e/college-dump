#!/usr/bin/env python3

s = input()
while s != "end":
  words = s.split()
  if words[0] == "3":
    print(" ".join(words))
  s = input()
