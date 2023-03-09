#!/usr/bin/env python3

s = input()

i = 0

j = 0

while i < len(s) and s != "end":
  while i < len(s) and s[i] != ":":
    i = i + 1
  print(s[:i])
  i = 0
  s = input()
