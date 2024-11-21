#!/usr/bin/env python3

def even_count(lst):
    curNode = lst.head
    count = 0
    while curNode is not None:
        if curNode.item % 2 == 0:
            count += 1
        curNode = curNode.next
    return count