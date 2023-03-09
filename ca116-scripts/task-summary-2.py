#!/usr/bin/env python3

import sys
newdict = {}
s = sys.stdin.readline().strip()

newdict = {}

a = []

while s != "":
  s = s.split(".py.")
  user = s[0]
  names = user.split("/")
  name = names[0]
  mark = s[1]
  if user not in newdict and mark == "correct":
    newdict[user] = 1
    a.append(name)
  elif user not in newdict and mark == "incorrect":
    newdict[user] = 0
    a.append(name)
  elif user in newdict and mark == "correct":
    newdict[user] += 1
  elif user in newdict and mark == "incorrect":
    newdict[user] = 0
  s = sys.stdin.readline().strip()

b = {}
i = 0
count = 0
while i < len(a):
  if a[i] not in b:
    b[a[i]] = 0
  i = i + 1
i = 0
c = {}
i = 0
while i < len(a):
  c[a[i]] = 0
  i = i + 1
e = []
i = 0
for key in newdict:
  e.append(key[:len(a[i])])
  e.append(newdict[key])
  i = i + 1
i = 0
while i < len(e):
  if e[i] in b:
    b[e[i]] += e[i + 1]
  i = i + 2

for key in b:
  print(key, b[key])
