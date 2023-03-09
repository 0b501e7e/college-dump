#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

nums = [int(line.strip()) for line in lines]

n = len(nums)
total = sum(nums)
mean = total / n

snums = sorted(nums)

if n % 2 == 1:
  median = snums[n // 2]
else:
  median = (snums[n // 2 - 1] + snums[n // 2]) / 2

print("Mean: {:.1f}".format(mean))
print("Median: {:.1f}".format(median))
