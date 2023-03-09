#!/usr/bin/env python3

print("Enter numbers (-1 to end): ", end="")
lst = []
num = int(input())
while num != -1:
  lst.append(num)
  num = int(input())

dupes = []
newlst = []
for x in lst:
  if x not in newlst:
    newlst.append(x)
  else:
    dupes.append(x)

for num in dupes:
  print(str(num) + " ", end="")
print()
