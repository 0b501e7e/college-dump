#!/usr/bin/env python3

s = input()

while s != "end":
  words = s.split()
  time = words[1]
  dur = words[2]
  time = int(time) * 100
  if dur == "1":
    dur = time + 50
  elif dur == "2":
    dur = time + 150
  elif dur == "3":
    dur = time + 250
  time = time / 100
  dur = int(dur) / 100
  newtime = str(time).split(".")
  newdur = str(dur).split(".")
  newtime = ":".join(newtime)
  newdur = ":".join(newdur)
  newtime = newtime + "0"
  newdur = newdur + "0"
  words[1] = newtime
  words[2] = newdur
  print(" ".join(words))
  s = input()
