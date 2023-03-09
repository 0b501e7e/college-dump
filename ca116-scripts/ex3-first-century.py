#!/usr/bin/env python3

import sys

a = []

s = sys.stdin.readlines()

i = 0
while i < len(s):
  if int(s[i]) >= 100:
    a.append(int(s[i]))
  i = i + 1
if len(a) == 0:
  print("none")
else:
  print(a[0])
