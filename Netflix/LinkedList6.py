import collections

class LinkedListNode(object):
    def __init__(self, key, value, freq):
        self.key = key
        self.val = value
        self.freq = freq
        self.next = None
        self.prev = None
    

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, node):
        node.next, node.perv = None, None
        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
    
    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.next, node.prev = None, None
