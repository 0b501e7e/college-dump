#!/usr/bin/env python3

import sys

censored = sys.argv[1]
text = sys.argv[3]

with open(text) as txt:
  text = txt.readlines()
for word in censored:
  word = word.strip()
  for word in text:
    text.replace(word, ("@" * len(word))

print(text)
