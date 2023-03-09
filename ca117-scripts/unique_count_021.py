#!/usr/bin/env python3

import sys
import string

lines = sys.stdin.read()

lines = lines.strip().translate(str.maketrans("", "", string.punctuation)).lower().split()

count_dict = {}

for word in lines:
  if word not in count_dict:
    count_dict[word] = 1

print(len(count_dict.keys()))
