#!usr/bin/env python3

import sys

lines = sys.stdin.readlines()

nums = lines[0].strip()

order = lines[1].strip()

new_nums = []
new_dict = {}
nums = nums.split()

for num in nums:
  new_nums.append(int(num))

new_nums.sort()


ordersort = "".join(sorted(order))
ordersort = [ordersort[0], ordersort[1], ordersort[2]]

i = 0
while i < len(ordersort):
  new_dict[ordersort[i]] = str(new_nums[i])
  i += 1
res = ""
for ord in order:
    res += new_dict[ord] + " "

print(res.strip())
