class Stack:
    def __init__(self, size):
        self.size = size 
        self.data = [] 
        self.top = -1 
    
    def __del__(self):
        del self.data 
    
    def push(self, x):
        if self.isFull(): 
            print("Stack overflow") 
        else: 
            self.top += 1 
            self.data.append(x) 
    
    def pop(self):
        if self.isEmpty():
            print("Stack underflow") 
            return None 
        else: 
            x = self.data[self.top] 
            self.top -= 1 
            self.data.pop() 
            return x 
    
    def isEmpty(self):
        return self.top == -1 
    
    def isFull(self):
        return self.top == self.size - 1 
