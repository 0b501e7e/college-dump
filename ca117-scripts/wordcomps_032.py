#!/usr/bin/env python3

import sys

def allvowels(w):
  return "a" in w and "e" in w and "i" in w and "o" in w and "u" in w

def ending(w):
  return w[-4:] == "iary"

def easye(w):
  return "e" in w
try:
  lines = sys.stdin.readlines()

  allv = [word.strip() for word in lines if allvowels(word.lower())]

  end = [word.strip() for word in lines if ending(word.strip().lower())]

  easy = [word.strip() for word in lines if easye(word.lower())]

  e = [word.strip() for word in easy if word.lower().count("e") == 5]

  print(f'Shortest word containing all vowels: {min(allv, key=len)}')
  print(f'Words ending in iary: {len(end)}')
  print(f"Words with most e's: {e}")

except FileNotFoundError:
  print(f'The file could not be found')
