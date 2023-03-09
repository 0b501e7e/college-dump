#!/usr/bin/env python3

n = int(input())

m = int(input())

i = 0

while i < n:
  print(m)
  if m % 2 == 0:
    m = int(m / 2)
  elif m % 2 == 1:
    m = int(m * 3) + 1
  i = i + 1
