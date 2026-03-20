class node(object):
    def __init__(self, data, n = None):
        self.data = data
        self.next_node = n

    def get_next(self):
        return self.next_node
    def set_next(self, n):
        self.next_node = n
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
class linkedlist(object):
    def __init__(self, r = None):
       self.root = r
       self.size = 0
    def get_size(self):
        return self.size
    def add(self, data):
        new_node = node(data, self.root)
        self.root = new_node
        self.size += 1
    def remove(self, data):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == data:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True #data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False #data not found
object = linkedlist()
object.add(10)
object.add(20)
object.add(30)
print(object.get_size())
print(object.remove(20))
print(object.get_size())  
print(object.remove(30))      
