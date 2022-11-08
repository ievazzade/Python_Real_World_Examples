import random

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.arbitrary = None

def insert_at_head(head, data):
    newNode = LinkedListNode(data)
    newNode.next = head
    return newNode

def insert_at_tail(head, node):
    if head is None:
        return node
    temp = head
    while temp.next != None:
        temp = temp.next

    temp.next = node
    return head

def create_random_list(length):
    list_head = None
    for x in range(length):
        list_head = insert_at_head(list_head, random.randrange(1,100))
    return list_head

def create_linked_list(lst):
    list_head = None
    for x in reversed(lst):
        list_head = insert_at_head(list_head, x)
    return list_head

def display(head):
    temp = head
    while temp:
        print(str(temp.data), end="")
        temp = temp.next
        if temp != None:
            print(", ", end="")
