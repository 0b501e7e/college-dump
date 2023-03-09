#!/usr/bin/env python3

class Contact(object):

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} {self.phone} {self.email}"


class ContactList(object):

    def __init__(self):
        self.d = {}

    def add_contact(self, C):
        self.d[C.name] = C

    def del_contact(self, name):
        if name in self.d:
            del self.d[name]

    def get_contact(self, name):
        if name in self.d:
            return self.d[name]
        else:
            return None

    def __str__(self):
        slist = list()
        print("Contact list")
        print("------------")
        for n, c in self.d.items():
            slist.append("{}".format(c))
        return "\n".join(sorted(slist))
