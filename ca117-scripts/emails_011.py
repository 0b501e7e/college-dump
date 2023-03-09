#!/usr/bin/env python3

import sys

emails = sys.stdin.readlines()

for email in emails:
  email = email.strip()
  i = 0
  while i < len(email) and email[i] != ".":
    i += 1
  if i < len(email):
    firstname = email[:i]
    lastname = email[i + 1:]
    i = 0
    while i < len(lastname) and lastname[i] < "0" or "9" < lastname[i]:
      i += 1
    if i < len(lastname):
      lastname = lastname[:i]
    name = " ".join([firstname, lastname])
    name = name.title()
    print(name)
