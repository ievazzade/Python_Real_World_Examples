from DLinkedList import *

class lru_structure:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {} # Hashmap
        self.cache_vals = DLinkedList() # Doubly linked list
    
    def Set(self, key, value):
        if key not in self.cache:
            if (self.cache_vals.size >= self.capacity):
                self.cache_vals.insert_at_tail(key, value)
                self.cache[key] = self.cache_vals.get_tail()
                del self.cache[self.cache_vals.get_head().key]
                self.cache_vals.remove_head()
            else:
                self.cache_vals.insert_at_tail(key, value)
                self.cache[key] = self.cache_vals.get_tail()
        else:
            self.cache_vals.remove_node(self.cache[key])
            self.cache_vals.insert_at_tail(key, value)
            self.cache[key] = self.cache_vals.get_tail()

    def Get(self, key):
        if key not in self.cache:
            return None
        else:
            value = self.cache[key].data
            self.cache_vals.remove_node(self.cache[key])
            self.cache_vals.insert_at_tail(key, value)
            return value
    
    def print_data(self):
        node = self.cache_vals.get_head()
        while node != None:
            print("(" + str(node.key) + "," + str(node.data) + ")", end ="")
            node = node.next
        print()

if __name__ == "__main__":
    obj = lru_structure(3)
    obj.Set(10, 20)
    obj.print_data()

    obj.Set(15, 25)
    obj.print_data()

    obj.Set(20, 30)
    obj.print_data()

    obj.Set(25, 35)
    obj.print_data()

    obj.Set(5, 40)
    obj.print_data()

    obj.Get(25)
    obj.print_data()