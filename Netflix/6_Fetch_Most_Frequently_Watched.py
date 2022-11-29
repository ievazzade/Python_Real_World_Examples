from LinkedList6 import *

class lfu_structure:
    def __init__(self, capacity):
        self.cap = capacity
        self.size = 0
        self.min_freq = 0
        self.freq_dict = collections.defaultdict(LinkedList)
        self.key_dict = {}
    
    def Get(self, key):
        if key not in self.key_dict:
            return None
        
        temp = self.key_dict[key]
        self.key_dict[key] = LinkedListNode(key, temp.val, temp.freq)
        self.freq_dict[temp.freq].delete(temp)