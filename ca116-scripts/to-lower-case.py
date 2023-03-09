#!/usr/bin/env python3

upper = "ABCDEFGHIJKLMNOPQRSTYVWXYZ"

lower = "abcdefghijklmnopqrstuvwxyz"

i = 0

j = 0

s = input()
output = s

while i < len(output) and output != "end":
  while i < len(output) and (output[i] >="a" and output[i] <= "z") or output[i] == " " or output[i] == "," or output[i] == ".":
    i = i + 1
  while output[i] != upper[j]:
    j = j + 1
  output = output[:i] + lower[j] + output[i + 1:]
  j = 0
  i = 0
print(output)
