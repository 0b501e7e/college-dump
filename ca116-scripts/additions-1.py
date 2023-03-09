#!/usr/bin/env python3

count = 10

i = 0

while i < count:
  j = 0
  s = input()
  while j < len(s) and (s[j] != "+"):
    j = j + 1
  total = int(s[:j]) + int(s[j + 1:])
  print(total)
  i = i + 1
