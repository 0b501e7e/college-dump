#!/usr/bin/env python3

from Stack import Stack

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def isempty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            print("The queue is empty")
            return

        elif len(self.stack2) == 0 and len(self.stack1) > 0:
            while len(self.stack1):
                tmp = self.stack1.pop()
                self.stack2.append(tmp)
            return self.stack2.pop()
        
        else:
            return self.stack2.pop()
