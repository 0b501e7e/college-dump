#!/usr/bin/env python3

n = int(input())

n = str(n)

total = 0

total = (n[-1] * 2 ** 0)
total = total + (n[-2] * 2 ** 1)
total = total + (n[-3] * 2 ** 2)
total = total + (n[-4] * 2 ** 3)
total = total + (n[-5] * 2 ** 4)
print(total) 
