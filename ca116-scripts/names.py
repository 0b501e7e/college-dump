#!/usr/bin/env python3

import sys

with open("boys.txt") as f:
  boys = f.readlines()

with open("girls.txt") as g:
  girls = g.readlines()

newdict = {}

i = 0

while i < len(boys):
  boys[i] = boys[i].strip()
  if boys[i] not in newdict:
    newdict[boys[i]] = "boy"
  i = i + 1

j = 0
while j < len(girls):
  girls[j] = girls[j].strip()
  if girls[j] not in newdict:
    newdict[girls[j]] = "girl"
    j = j + 1
  else:
    newdict[girls[j]] = "either"
    j = j + 1
a = []

names = sys.stdin.readline().strip()
while names != "":
  a.append(names)
  names = sys.stdin.readline().strip()

i = 0

while i < len(a):
  person = a[i]
  if person in newdict:
    print(person, newdict[person])
  i = i + 1
