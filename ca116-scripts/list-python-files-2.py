#!/usr/bin/env python3

import os

files = os.listdir(".")
i = 0

while i < len(files):
  file = files[i]
  filesize = os.path.getsize(file)
  if filesize > 0 and (file[-3:] == ".py"):
    print(file)
  i = i + 1
