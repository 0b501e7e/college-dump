#!/usr/bin/env python3

s = input()

while s != "end":
  t = ""
  i = 0
  while i < len(s) and (s[i] != ","):
    i = i + 1
  if s[i + 1:i + 3] == "WI":
    t = s[:i]
    print(t)
    s = input()
  else:
    s = input()
