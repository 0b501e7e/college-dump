import sys

f1 = sys.argv[1]
f2 = sys.argv[2]

with open(f1) as f:
    data1 = f.read().strip().split("\n")

with open(f2) as f:
    data2 = f.read().strip().split("\n")

def compare(data1, data2):
    names = []

    for n in data1:
        if n in data2:
            names.append(n)
    names.sort()
    for i, name in enumerate(names):
        print(f"{i+1}. {name}")

compare(data1, data2)
