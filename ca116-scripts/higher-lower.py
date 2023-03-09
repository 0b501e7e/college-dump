#!/usr/bin/env python3

n = int(input())

i = 0

while i < 5:
  m = int(input())
  if m > n:
    print("higher")
  elif m < n:
    print("lower")
  else:
    print("equal")
  n = m
  i = i + 1
