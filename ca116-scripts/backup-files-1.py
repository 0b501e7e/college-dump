#!/usr/bin/env python3

import os
import sys


files = os.listdir(".")

i = 0
while i < len(files):
  file = files[i]
  lastbak = file[len(file) - 4:]
  secondbak = file[len(file) - 8: len(file) - 4]
  if lastbak != ".bak" and secondbak != ".bak":
    with open(file) as f:
      copy = f.read()
    filename = file + ".bak"
    with open(filename, "w") as g:
      g.write(copy)
  i = i + 1
