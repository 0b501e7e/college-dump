#!/usr/bin/env python3

def get_plural(word):
  es = ["ch", "sh", "x", "s", "z"]
  vowels = ["a", "e", "i", "o", "u"]
  ves = ["f", "fe"]
  es1 = ["o"]
  if word[-1] in es[2:]:
    return word + "es"
  elif word[-2:] in es[:2]:
    return word + "es"
  elif word[-2] not in vowels and word[-1] == "y":
    return word[:-1] + "ies"
  elif word[-1] in ves:
    return word[:-1] + "ves"
  elif word[-2:] in ves:
    return word[:-2] + "ves"
  elif word[-1] in es1:
    return word + "es"
  else:
    return word + "s"
