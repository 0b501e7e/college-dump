#!/usr/bin/env python3

s = input()

a = "a"

b = "b"

c = "c"

d = "d"

e = "e"

f = "f"

g = "g"

i = 0

t = ""
while i < len(s):
  if s[i] == a:
    t = t + a
  elif s[i] == b:
    t = t + b
  elif s[i] == c:
    t = t + c
  elif s[i] == d:
    t = t + d
  elif s[i] == e:
    t = t + e
  elif s[i] == f:
    t = t + f
  elif s[i] == g:
    t = t + g
  i = i + 1

print(t[0])
