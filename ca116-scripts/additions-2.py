#!/usr/bin/env python3

total = 0
i = 0
j = 0
s = input()

while j < 5:
  while i < len(s) and s[i] != "+":
    i = i + 1

  if i < len(s):
    k = i
    i = 0
    total = total + int(s[0:k])
    s = s[(k + 1)::]
    j = j + 1
  else:
      total = total + int(s)
      j = 5

print(total)
