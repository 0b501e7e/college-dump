#!/usr/bin/env python3

s = input()

i = 0

j = 0

k = 0

l = 0
day = ""

number = ""

month = ""

while i < len(s) and s[i] != " ":
  i = i + 1

if i < len(s):
  day = s[0:i]
  j = i + 1

while j < len(s) and s[j] != " ":
  j = j + 1

if j < len(s):
  number = s[(i + 1):j]
  k = j + 1

while k < len(s) and s[k] != " " and s[k] != ",":
  k = k + 1

if k < len(s):
  month = s[(j + 1):k]
  l = k + 2

year = s[l::]

print(month, number + ",", year, "(" + day + ")")
