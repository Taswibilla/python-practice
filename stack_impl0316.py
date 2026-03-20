class stack(object):
    #constructor
    def __init__(self):
        self.stack = [] 
        self.numofitems = 0
    #checking empty
    def isEmpty(self):
        return self.stack == []
    #pushing element
    def push(self, data):
        self.stack.insert(self.numofitems,data)
        self.numofitems += 1
        return '{} pushed to stack'.format(data)
    #popping element
    def pop(self):
        if self.isEmpty():
            return 'Stack is empty'
        else:
            self.numofitems -= 1
            return '{} popped from stack'.format(self.stack.pop())  
    def stacksize(self):
        return len(self.stack)
#testing the stack
if __name__ == "__main__":    
    s = stack()
    print(s.push(10))
    print(s.push(20))
    print(s.push(30))
    print(s.pop())
    print(s.stacksize())