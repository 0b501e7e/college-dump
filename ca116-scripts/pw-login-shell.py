#!/usr/bin/env python3

s = input()

i = 0

j = 0

while i < len(s) and s != "end":
  while i < len(s) and s[i] != ":":
    i = i + 1
  while j < len(s) and s[j] != ":":
    j = j - 1
  print(s[:i], s[j + 1:])
  i = 0
  j = 0
  s = input()
