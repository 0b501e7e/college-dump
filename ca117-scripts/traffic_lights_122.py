#!/usr/bin/env python3

import sys

# read stdin into a list

lines = sys.stdin.readlines()

# length of road
rd_len = lines[0]

# processing the lines for traffic light data
for line in lines[1:]:
    [d, r, g] = line.strip().split()
    cycle = int(r) + int(g)     # cycle is the total time it takes to repeat the on/off of a light
    pos = 0
    time = 0
    while pos <= int(rd_len):
        time += 1
        pos += 1
        if pos == d and time % cycle != 0:   # if time doesn't divide evenly into cycle we know its red
            diff = int(r) - time
            if diff < 0:
                diff *= -1
            time += diff
        elif pos == d and time % cycle == 0:
            time += 1
            pos += 1
        pos += 1
        time += 1
print(time)
