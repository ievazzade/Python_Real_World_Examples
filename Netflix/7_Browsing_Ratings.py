from Stack import my_stack

class max_stack:
    def __init__(self):
        self.max_stack = my_stack()
        self.main_stack = my_stack()
        return
    
    def pop(self):
        self.max_stack.pop()
        return self.main_stack.pop()
    
    def push(self, value):
        self.main_stack.push(value)
        if (self.max_stack.is_empty() or self.max_stack.top() < value):
            self.max_stack.push(value)
        else:
            self.max_stack.push(self.max_stack.top())
        
    def max_rating(self):
        if not self.max_stack.is_empty():
            return self.max_stack.top()
        
if __name__ == "__main__":
    ratings = max_stack()
    ratings.push(5)
    ratings.push(0)
    ratings.push(2)
    ratings.push(4)
    ratings.push(6)
    ratings.push(3)
    ratings.push(10)

    print(ratings.main_stack.stack_list)
    print("Maximum Rating: " + str(ratings.max_rating()))

    ratings.pop() # Back button effect
    print("\nAfter clicking back button\n")
    print(ratings.main_stack.stack_list)
    print("Maximum value: " + str(ratings.max_rating()))