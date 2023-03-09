#!/usr/bin/env python3

i = 0

pos = 0

neg = 0

while i < 5:
  n = int(input())
  if n < 0:
    neg = neg + n
  else:
    pos = pos + n
  i = i + 1

print(neg, pos)
