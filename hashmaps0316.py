class HashMap:
    def __init__(self):
        self.map = {}          # internal dictionary
        self.num_of_items = 0  # count of items

    # Check if empty
    def is_empty(self):
        return self.num_of_items == 0

    # Add or update key-value
    def put(self, key, value):
        if key not in self.map:
            self.num_of_items += 1
        self.map[key] = value
        return "'{}': '{}' added".format(key, value)

    # Get value by key
    def get(self, key):
        if key in self.map:
            return self.map[key]
        else:
            return "'{}' not found".format(key)

    # Remove key-value pair
    def remove(self, key):
        if key in self.map:
            self.num_of_items -= 1
            return "'{}': '{}' removed".format(key, self.map.pop(key))
        else:
            return "'{}' not found".format(key)

    # Number of items
    def size(self):
        return self.num_of_items

# Testing the basic HashMap
if __name__ == "__main__":
    hm = HashMap()
    print(hm.put("apple", 10))
    print(hm.put("banana", 20))
    print(hm.get("apple"))
    print(hm.remove("banana"))
    print("Size:", hm.size())
    print("Is empty?", hm.is_empty())