#!/usr/bin/env python3

def sumto(a, b):
  c = a
  if a == b or a > b:
    print(c)
  else:
    c += a
    sumto(a+1, b)

sumto(4, 7)
