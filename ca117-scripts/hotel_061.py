#!/usr/bin/env python3

import sys

lines = sys.stdin

for line in lines:
  line = line.split()
  amt, taken = line[0], line[1:]

range = [i for i in range(1, int(amt) + 1)]

vacancy = [num for num in range if str(num) not in taken]

if len(vacancy) > 0:
  print(min(vacancy))
else:
  print("no room")
