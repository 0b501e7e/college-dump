#!/usr/bin/env python3

import os

files = os.listdir(".")

i = 0

while i < len(files):
  file = files[i]
  if file[-3:] == ".py":
    print(file)
  i = i + 1
