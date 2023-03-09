#!/usr/bin/env python3

import sys

file = sys.argv[1]
try:
  with open(file) as f:
    results = f.readlines()
  highest = 0

  for line in results:
    try:
      line = line.split(" ", 1)
      mark = line[0]
      name = line[1]
      if int(mark) > int(highest):
        highest = mark
    except ValueError:
      print(f'Invalid mark {mark} encountered. Skipping.')
  best_students = []
  for line in results:
    tokens = line.split(" ", 1)
    mark = tokens[0]
    name = tokens[1].strip()
    if mark == highest:
      best_students.append(name)

  print(f'Best student(s): {", ".join(best_students)}')
  print(f'Best mark: {highest}')

except FileNotFoundError:
  print(f'The file {file} does not exist.')
