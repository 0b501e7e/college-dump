
#!user/bin/env python3

s = input()


l = len(s)

first = s[:(len(s) // 3)]

second = s[len(first):len(first) * 2 ]

third = s[len(first) + len(second):]

words = [first, second, third]

newdict = {}

i = 0
while i < len(words):
  word = words[i]
  if word not in newdict:
    newdict[word] = 1
    i = i + 1
  else:
    newdict[word] += 1
    i = i + 1
for word in newdict:
  if newdict[word] > 1:
    print(word)
