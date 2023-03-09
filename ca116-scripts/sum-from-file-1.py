#!/usr/bin/env python3

with open("numbers.txt") as f:
  lines = f.readlines()

i = 0

count = 0

while i < len(lines):
  count = count + int(lines[i])
  i = i + 1

print(count)
