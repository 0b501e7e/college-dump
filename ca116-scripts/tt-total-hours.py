#!/usr/bin/env python3

s = input()

hours = 0

while s != "end":
  words = s.split()
  hours = hours + int(words[2])
  s = input()

print(hours)
