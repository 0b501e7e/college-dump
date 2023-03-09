#!/usr/bin/env python3

import sys

german = {"one": "eins", "two": "zwei",
          "three": "drei", "four": "vier",
          "five": "funf", "six": "sechs",
          "seven": "sieben", "eight": "acht",
          "nine": "neun", "ten": "zehn", }
a = []
word = sys.stdin.readline().rstrip()
while word != "":
  if word in german:
    a.append(german[word])
  word = sys.stdin.readline().rstrip()

i = 0
while i < len(a):
  print(a[i])
  i = i + 1
