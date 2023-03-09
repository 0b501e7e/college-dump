#!/usr/bin/env python3

s = input()

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

trufalse = True

i = 0

while trufalse:
  j = 0
  while(j < 26 and trufalse):
    if (s[i] == alpha[j]):
      print(i)
      trufalse = False
    j = j + 1
  i = i + 1
