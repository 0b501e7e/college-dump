#!/usr/bin/env python3

import sys

num_lines = sys.stdin.readlines()

d = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}

for line in num_lines:
  line = line.strip().split()
  res = [d[int(num)] if num.isnumeric() and int(num) in range(11) else "unknown" for num in line]
  print(" ".join(res))
