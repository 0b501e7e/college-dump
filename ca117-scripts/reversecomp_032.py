#!/usr/bin/env python3

def binsearch(query, sorted_list):

  low = 0
  high = len(sorted_list) - 1

  while low <= high:
    mid = (low + high) // 2
    if sorted_list[mid] < query:
      low = mid + 1
    elif sorted_list[mid] > query:
      high = mid - 1
    else:
      return True
  return False

import sys

words = sys.stdin.readlines()

l = [line.strip() for line in words]
sl = sorted([w.lower() for w in l])
revs = [w for w in l if len(w) >= 5 and binsearch(w[::-1].lower(), sl)]
print(revs)
