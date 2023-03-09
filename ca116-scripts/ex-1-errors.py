#!/usr/bin/env python3

n = int(input())

m = 253842

i = 0

while i < n:
  v = int(input())
  m = (m + v) * 300064 - 104182
  print(v * 272808)
  i = i + 1

print(m)
