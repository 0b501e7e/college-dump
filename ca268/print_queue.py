#!/usr/bin/env python3

class Queue:
    def __init__(self, capacity = 4):
        self.data = [0] * capacity
        self.front = 0
        self.back = 0

    def count(self):
        if self.back >= self.front:
            return self.back - self.front
        else:
            return self.back - self.front + len(self.data)

    def isempty(self):
        return self.front == self.back

    def enqueue(self, item):
        if self.count() < len(self.data) - 1:
            self.data[self.back] = item
            self.back = (self.back + 1) % len(self.data)
        else:
            print("Queue Full")

    def dequeue(self):
        if self.count() > 0:
           item = self.data[self.front]
           self.front = (self.front + 1) % len(self.data)
           return item
        else:
            return None

def print_queue(l, f, b):
    for num in l:
        print(num)


size = int(input())
q = Queue(size)

command = input()
while len(command) > 0:
    if command[0] == 'a': # add
        item = command.split()[1]
        q.enqueue(int(item));
    elif command[0] == 'r': # remove
        q.dequeue();
    else:
        print("Unknown command!")
        command = input()

print_queue(q.data, q.front, q.back)
