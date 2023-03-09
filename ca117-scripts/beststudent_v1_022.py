#!/usr/bin/env python3

import sys

file = sys.argv[1]
try:
  with open(file) as f:
    results = f.readlines()
  highest = 0

  for line in results:
    line = line.split(" ", 1)
    mark = line[0]
    name = line[1]
    if int(mark) > int(highest):
      highest = mark

  for line in results:
    tokens = line.split(" ", 1)
    mark = tokens[0]
    name = tokens[1].strip()
    if mark == highest:
      print(f'Best student: {name}')
      print(f'Best mark: {mark}')
      break

except FileNotFoundError:
  print(f'The file {file} does not exist')
