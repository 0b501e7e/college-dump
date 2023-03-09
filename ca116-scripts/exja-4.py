#!/usr/bin/env python3

import sys

line = sys.stdin.readline()

i = 0
while i < len(line) and line[i] != '"':
  i = i + 1

if i < len(line):
  line = line[i + 1:]

i = 0
while i < len(line) and line[i] != '"':
  i = i + 1

if i < len(line):
  print(line[:i])
