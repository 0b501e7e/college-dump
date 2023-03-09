#!/usr/bin/env python3

class Patient(object):

    def __init__(self, name, age, doctor, meds=None):
        self.name = name
        self.age = age
        self.doctor = doctor
        if meds is None:
            self.meds = []

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nMedications: {[i for i in self.meds]}\nDoctor: {self.doctor}"


p1 = Patient('Mary', 34, 'James Kildare', ["aspirin"])
p2 = Patient('Wendy', 40, 'Gregory House', ["penicillin", "nexium"])
assert (p1.name == 'Mary')
assert (p1.age == 34)
assert (p1.doctor == 'James Kildare')

print(p1)
print(p2)
