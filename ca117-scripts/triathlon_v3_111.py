#!/usr/bin/env python3

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.d = {}

    def race_time(self):
        return sum(self.d.values())

    def add_time(self, dis, time=0):
        self.dis = dis
        self.time = time
        self.d[dis] = time

    def get_time(self, dis):
        return self.d[dis]

    def __eq__(self, other):
        return self.race_time() == other.race_time()

    def __lt__(self, other):
        return self.race_time() < other.race_time()

    def __gt__(self, other):
        return self.race_time() > other.race_time()

    def __str__(self):
        return f"Name: {self.name}\nID: {self.tid}\nRace time: {self.race_time()}"


class Triathlon(object):

    def __init__(self):
        self.d = {}

    def add(self, t):
        self.d[t.tid] = t

    def remove(self, t):
        del self.d[t]

    def lookup(self, t):
        if t in self.d:
            return self.d[t]
        else:
            return None

    def best(self):
        lst = []
        for t in self.d.values():
            lst.append((t.race_time(), t.tid))
        lst.sort()
        lst2 = [time for name, time in lst]
        best = lst2[0]
        if best in self.d:
            return self.d[best]

    def worst(self):
        lst = []
        for t in self.d.values():
            lst.append((t.race_time(), t.tid))
        lst.sort()
        lst2 = [time for name, time in lst]
        worst = lst2[-1]
        if worst in self.d:
            return self.d[worst]

    def __str__(self):
        lst = []
        for tid, t in self.d.items():
            lst.append(f"Name: {t.name}\nID: {tid}\n")
            lst.sort()
        return "".join(lst).strip()
