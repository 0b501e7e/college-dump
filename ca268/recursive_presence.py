#
#  Just a class to store the item and the next pointer
#
import sys

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

# Note, these are methods "A method is a function that is stored as a class attribute"
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next    # remove the item by moving the head pointer
            return item

    def is_empty(self):
        return self.head == None

    def is_present(self, item):
        if self.head is None:
            return False
        elif self.head.item == item:
            return True
        else:
            self.head = self.head.next
            return self.is_present(item)

def main():
    # Read each set
    line = sys.stdin.readline()
    items = line.strip().split()
    
    ll = LinkedList()
    problem = False
    if ll.is_present(items[0]):
        print("An empty list should not match anything")
        problem = True
    
    else:
        for item in items:
            if ll.is_present(item):
                print(item + " detected before being added.")
                problem = True
            ll.add(item)
            
        # Now every item in the items should be in the list.
        for item in items:
            if not ll.is_present(item): # item should not be contained
                print(item + " not found in list.")
                problem = True

    if not problem:
        # check that the list still contains all the items
        while not ll.is_empty() and len(items) > 0:
            if ll.remove() != items.pop():
                print("List has been modified")
                problem = True
                break
        
        if not problem:
            if (not ll.is_empty()) or len(items) != 0:
                print("the list size is wrong");
                problem = True
                
    if problem:
        print("More work nned!")
    else:
        print("all ok!")

if __name__ == "__main__":
    main()