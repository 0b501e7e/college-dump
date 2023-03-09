#!/usr/bin/env python3

import sys

def tagger(item):
  return item[1]
lines = sys.stdin.readlines()

d = {}
disq = []
for line in lines:
  line = line.strip()
  name, shots = line[:-5].strip(), line[-5:]
  shots = shots.split()
  for shot in shots:
    if not shot.isnumeric():
      disq.append(name)
  shots = [int(shot) for shot in shots if shot.isnumeric()]
  d[name] = sum(shots)

for k, v in sorted(d.items(), key=tagger):
  if k in disq:
    continue
  print(f'{k}: {v}')

if len(disq) > 0:
  print(f'Disqualified: {", ".join(disq)}')
