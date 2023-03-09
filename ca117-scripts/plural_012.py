#!/usr/bin/env python3

import sys

nouns = sys.stdin.readlines()

cons = "bcdfghjklmnpqrstvwxyz"

for noun in nouns:
  noun = noun.strip().lower()
  end = noun[-2:]
  if end == "ch" or end == "sh":
    print(noun + "es")
    continue
  elif noun[-1] == "x" or noun[-1] == "s" or noun[-1] == "z":
    print(noun + "es")
    continue
  if noun[-2] in cons and noun[-1] == "y":
    print(noun[:-1] + "ies")
    continue
  if noun[-1] == "f":
    print(noun[:-1] + "ves")
    continue
  elif noun[-2:] == "fe":
    print(noun[:-2] + "ves")
    continue
  if noun[-1] == "o":
    print(noun + "es")
    continue
  else:
    print(noun + "s")
    continue
