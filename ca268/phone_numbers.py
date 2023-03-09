#!/usr/bin/env python3

command = input("Enter a name and number, or a name and ? to query (!! to exit)\n")
newdict = {}
while command != "!!":

  token = command.split()
  if token[1] != "?":
    newdict[token[0]] = token[1]

  if token[1] == "?":
    if token[0] in newdict:
      print(f'{token[0]} has number {newdict[token[0]]}')
    else:
      print(f'Sorry, there is no {token[0]}')
  command = input()

if command == "!!":
  print("Bye")
