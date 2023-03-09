#!/usr/bin/env python3

n = int(input())

i = 0

j = 1

l = 0

count = 0
while i < n:
  print(l)
  count = l + j
  l = j
  j = count
  i = i + 1
