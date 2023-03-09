#!/usr/bin/env python3

n = int(input())

i = 0

total = 0

while i < n:
  o = input()
  if o == "one":
    o = 1
  elif o == "two":
    o = 2
  elif o == "three":
    o = 3
  elif o == "four":
    o = 4
  elif o == "five":
    o = 5
  total = total + o
  i = i + 1

print(total)
