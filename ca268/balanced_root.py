class Node:
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    """ An implementation of a Binary Search Tree
     """
    def __init__(self, lst = None):
        self.root = None
        if lst != None:
            for x in lst:
                self.add(x)

    def recurse_add(self, ptr, item):
        if ptr == None:
            return Node(item)
        elif item < ptr.item:
            ptr.left = self.recurse_add(ptr.left, item)
        elif item > ptr.item:
            ptr.right = self.recurse_add(ptr.right, item)
        return ptr
        
    def add(self, item):
        """ Add this item to its correct position on the tree """
        self.root = self.recurse_add(self.root, item)

    def r_height(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + max(self.r_height(ptr.left), self.r_height(ptr.right))

    def height(self): 
        return self.r_height(self.root)
    
    def is_avl(self):
        if self.root is None:
            return True
        else:
            left_height = self.r_height(self.root.left)
            right_height = self.r_height(self.root.right)
import sys



def main():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items]

    tree = BST(nums)

    if tree.height() > 2:
         print("error ... your tree is too tall")
    else:
         print(tree.is_avl())

if __name__ == "__main__":
    main()
