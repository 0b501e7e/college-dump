#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

word2num = {}

for line in lines:
  line = line.split()

  # if the line starts with def, split the line and map the key values to a dictionary

  if line[0] == "def":
    word2num[line[1]] = line[2]

  # if the line starts with calc, calculate the expression in the line

  if line[0] == "calc":
    expression = line[1:-1]
    for index, word in enumerate(expression):
      if word in word2num:
        expression[index] = word2num[word]
    expression = " ".join(expression)
    try:
      keys = list(word2num.keys())
      vals = list(word2num.values())
      try:
        position = vals.index(str(eval(expression)))
        print(" ".join(line[1:]), keys[position])
      except ValueError:
        print(" ".join(line[1:]), "unknown")
    except NameError:
      print(" ".join(line[1:]), "unknown")

  # clear all existing definitions

  if line[0] == "clear":
    for elem in dir():
      if elem[:2] != "__":
        del globals()[elem]
