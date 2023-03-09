#!/usr/bin/env python3

with open("irish-dobs.txt") as f:
  lines = f.readlines()

i = 0
a = []
k = 0
fname = "american-dobs.txt"

while i < len(lines):
  s = lines[i]
  s = s.split()
  name = " ".join(s[1:])
  date = s[0]
  date = date.split("/")
  tmp = date[0]
  date[0] = date[1]
  date[1] = tmp
  date = "/".join(date)
  newdata = (date + " " + name)
  a.append(newdata)
  i = i + 1

with open(fname, "w") as g:
  while k < len(a):
    g.write(a[k] + "\n")
    k = k + 1
