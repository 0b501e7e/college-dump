#!/usr/bin/env python3

if x == y and y == z:
  print("equilateral")

elif (x == y or x == z) or (y == x or y == z) or (z == x or z == y):
  print("isosceles")

else:
  print("scalene")
