#!/usr/bin/env python3

import sys

newdict = {}

contacts = sys.argv[1]

with open(contacts) as f:
  lines = f.readlines()

for line in lines:
  line = line.split()
  name, number, email = line[0], line[1], line[2]
  newdict[name] = [number, email]

names = sys.stdin.readlines()

for x in names:
  x = x.strip()
  try:
    print(f'Name: {x}')
    print(f"Phone: {newdict[x][0]}")
    print(f'Email: {newdict[x][1]}')
  except KeyError:
    print('No such contact')
