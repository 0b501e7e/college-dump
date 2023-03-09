#!/usr/bin/env python3

def sum_to_k(lst, k):
  i = 0
  j = len(lst) - 1
  while i < j:
      if lst[i] + lst[j] == k:
          return True
      elif lst[i] + lst[j] < k:
          i += 1
      else:
          j -= 1
  return False
