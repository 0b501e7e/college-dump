#!/usr/bin/env python3

import os
import sys


files = os.listdir(".")

i = 0
while i < len(files):
  file = files[i]
  lastbak = file[len(file) - 4:]
  secondbak = file[len(file) - 8: len(file) - 4]
  if os.path.isfile(file) is True:
    if lastbak == ".bak":
      os.unlink(file)
  i = i + 1
