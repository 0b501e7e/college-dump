#!/usr/bin/env python3

n = int(input())

while n != 0:
  m = int(input())
  if m > n:
    print("higher")
  elif m < n and m != 0:
    print("lower")
  elif m == n:
    print("equal")
  n = m
