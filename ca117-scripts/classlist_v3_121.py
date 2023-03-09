#!/usr/bin/env python3

class Student(object):

    def __init__(self, name, address, sid):
        self.name = name
        self.address = address
        self.sid = sid
        self.d = {}
        self.mods = []

    def add_mark(self, module, mark):
        self.d[module] = mark
        if module not in self.mods:
            self.mods.append(module)

    def get_mark(self, module):
        if module in self.d:
            return self.d[module]
        else:
            return "Not registered for module"

    def __eq__(self, other):
        return self.average() == other.average()

    def __lt__(self, other):
        return self.average() < other.average()

    def __gt__(self, other):
        return self.average() > other.average()

    def total(self):
        return sum(self.d.values())

    def average(self):
        total = sum(self.d.values())
        leng = len(self.d.values())
        if leng > 0:
            average = total / leng
            return average
        else:
            return 0

    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}\nID: {self.sid}\n"


class Classlist(object):

    def __init__(self):
        self.d = {}
        self.mods = []

    def add(self, s):
        self.d[s.sid] = s

    def remove(self, s):
        if s in self.d:
            del self.d[s]

    def lookup(self, s):
        if s in self.d:
            return self.d[s]
        else:
            return None

    def least_popular_module(self):
        lst = []
        for s in self.d.values():
            for mod in s.mods:
                lst.append(mod)
        newd = {}
        for i in lst:
            if i not in newd:
                newd[i] = 1
            else:
                newd[i] += 1
        return sorted(newd)[-1]

    def __str__(self):
        lst = []
        for sid, name in self.d.items():
            lst.append(sid)
        lst.sort()
        lst2 = []
        for id in lst:
            lst2.append(f"{self.lookup(id)}")
        return "".join(lst2).strip()
