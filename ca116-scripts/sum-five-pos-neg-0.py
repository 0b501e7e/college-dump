#!/usr/bin/env python3

pos = 0

neg = 0

n = int(input())

while n != 0:
  if n < 0:
    neg = neg + n
  else:
    pos = pos + n
  n = int(input())

print(neg, pos)
