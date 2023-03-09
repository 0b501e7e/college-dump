#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for line in lines:
    line = line.strip().split()
    pOne, pTwo = line[0], line[1]
    if pOne == "paper" and pTwo == "rock":
        print("Player 1 wins")
    elif pOne == "rock" and pTwo == "paper":
        print("Player Two wins")
    elif pOne == pTwo:
        print("Draw")
        continue
    if pOne == "scissors" and pTwo == "paper":
        print("Player 1 wins")
    elif pOne == "paper" and pTwo == "scissors":
        print("Player 2 wins")
    elif pOne == pTwo:
        print("Draw")
        continue
    if pOne == "scissors" and pTwo == "rock":
        print("Player 2 wins")
    elif pOne == "rock" and pTwo == "scissors":
        print("Player 1 wins")
    elif pOne == pTwo:
        print("Draw")
        continue
