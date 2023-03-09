#!/usr/bin/env python3

s = input()

i = 0

tru = True

while (tru is True):
  j = 0
  while j < len(s) and (s[j] != "+"):
    j = j + 1
  total = int(s[:j]) + int(s[j + 1:])
  if total != 1000:
    print(total)
    i = i + 1
    s = input()
  else:
      print(total)
      tru = False
