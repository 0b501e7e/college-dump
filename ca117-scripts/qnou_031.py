#!/usr/bin/env python3

import sys

def qnou(s):
  s = s.replace("qu", "__")
  return "q" in s

lines = sys.stdin.readlines()

qnous = [word.strip() for word in lines if qnou(word.lower())]

print(f'Words with q but no u: {qnous}')
