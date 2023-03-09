#!/usr/bin/env python3

import sys

txt = sys.stdin.read()

tokens = txt.strip().split()

print(len(tokens))
