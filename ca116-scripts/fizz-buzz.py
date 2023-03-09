#!/usr/bin/env python3

n = int(input())

i = 0

j = 1

while i < n:
  if j % 3 == 0 and j % 5 != 0:
    print("fizz")
  elif j % 5 == 0 and j % 3 != 0:
    print("buzz")
  elif j % 3 == 0 and j % 5 == 0:
    print("fizz-buzz")
  else:
    print(j)
  i = i + 1
  j = j + 1
