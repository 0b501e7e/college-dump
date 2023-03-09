#!/usr/bin/env python3

import sys

input = sys.stdin.readlines()

print(f'Words containing 17 letters: {[i.strip() for i in input if len(i.strip()) == 17]}')
print(f'Words containing 18+ letters: {[i.strip() for i in input if len(i.strip()) >= 18]}')
print(f"Words with 4 a's: {[i.strip() for i in input if i.strip().lower().count('a') == 4]}")
print(f"Words with 2+ q's: {[i.strip() for i in input if i.strip().lower().count('q') >= 2]}")
print(f'Words containing cie: {[i.strip() for i in input if "cie" in i.strip().lower()]}')
print(f'Anagrams of angle: {[i.strip() for i in input if sorted(i.lower().strip()) == sorted("angle") and i.lower().strip() != "angle"]}')
