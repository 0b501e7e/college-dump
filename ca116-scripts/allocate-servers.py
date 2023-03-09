#!/usr/bin/env/ python3

s = input()

a = []

while s != "end":
  a.append(int(s))
  s = input()

count = 1

i = 0

while i < len(a):
  tmp = a[i] + 1000
  j = i + 1
  if a[j] < tmp:
    count = count + 1
  i = i + 1

print(count)
