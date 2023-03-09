#!/usr/bin/env python3

def l2d(file):
  lines = file.readlines()
  first = lines[0].strip().split()
  second = lines[1].strip().split()
  newdict = dict(zip(first, second))
  return newdict
