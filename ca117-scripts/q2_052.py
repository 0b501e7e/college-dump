#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

nums, order = lines[0], lines[1]

nums = sorted(nums.strip().split(), reverse=True)

srtorder = sorted(order.strip())

res = {srtorder[i]: nums[i] for i in range(len(srtorder))}

ans = []

for i in srtorder:
  ans.append(res[i])

print(" ".join(ans))
