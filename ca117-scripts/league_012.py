#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

pos = "POS"
club = "CLUB"
p = "P"
w = "W"
d = "D"
l = "L"
gf = "GF"
ga = "GA"
gd = "GD"
pts = "PTS"

team_names = []
longline = 0
team_list = []
for line in lines:
  tokens = line.strip().split()
  for token in tokens:
    if token.lstrip("-").isdigit()is False:
      team_names.append(token)
  team = " ".join(team_names)
  team_list.append(team)
  team_names = []

for team in team_list:
  if len(team) > longline:
    longline = len(team)

print(f'{pos:>s} {club:<{longline}s} {p:>2s} {w:>3s} {d:>3s} {l:>3s} {gf:>3s} {ga:>3s} {gd:>3s} {pts:>3s}')

team_names = []

for line in lines:
  tokens = line.strip().split()
  for token in tokens:
    if token.lstrip("-").isdigit() is False:
      team_names.append(token)
  team = " ".join(team_names)
  rank = tokens[0]
  played, won, drawn, lost, goalsfor, goalsagainst, goaldiff, points = (tokens[-8], tokens[-7], tokens[-6], tokens[-5], tokens[-4], tokens[-3], tokens[-2], tokens[-1])
  print(f'{rank:>3s} {team:<{longline}s} {played:>2s} {won:>3s} {drawn:>3s} {lost:>3s} {goalsfor:>3s} {goalsagainst:>3s} {goaldiff:>3s} {points:>3s}')
  team_names = []
