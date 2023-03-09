#!/usr/bin/env python3

import sys
a = []
b = []
c = []
line = sys.stdin.readline().strip()
i = 0
while line != "":
  line = line.split("/")
  user = line[0]
  c.append(user)
  file = line[1]
  file = file.split(".py.")
  program = file[0]
  mark = file[1]
  a = [user, program, mark]
  b.append(a)
  line = sys.stdin.readline().strip()

i = 0
d = []
while i < len(c):
  j = 0
  while j < len(d) and d[j] != c[i]:
    j = j + 1
  if j == len(d):
    d.append(c[i])
  i = i + 1


j = 0
i = 0
while j < len(d):
  i = 0
  while i < len(b):
    while i < len(b) and (b[i][0] != d[j]):
      i = i + 1
    if i < len(b):
      print(b[i])
    i = i + 1
  j = j + 1

