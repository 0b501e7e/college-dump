#!/usr/bin/env python3

def build_dictionary(stream):
  d = {}
  for line in stream:
    line = line.strip().split()
    d[line[0]] = line[1]
  return d

def extract_range(d, low, high):
  nd = {}
  for (key, val) in d.items():
    if int(val) >= low and int(val) <= high:
      nd[key] = val
  return nd
