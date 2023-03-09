#!/usr/bin/env python3

s = input()

a = []

b = []

i = 0


if s != "end":
  a.append(s)

while s != "end":
  s = input()

  while s != "end":
    while i < len(a) and s != a[i]:
      i = i + 1
    if i < len(a):
      b.append(s)
      i = 0
      s = input()
    else:
      a.append(s)
      i = 0
      s = input()

while i < len(a):
    print(a[i])
    i = i + 1
