#!/usr/bin/env python3

import os
import sys
files = os.listdir(".")

i = 0

while i < len(files):
  file = files[i]
  with open(file) as f:
    line = f.readline().strip()
  if (line == "#!/usr/bin/env python3" or file[-3:] == ".py"):
    if len(line) != 0:
      print(file)
  i = i + 1
