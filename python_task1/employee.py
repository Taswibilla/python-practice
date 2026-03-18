class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

    def __add__(self, other):
        return self.salary + other.salary

    def __len__(self):
        return len(self.name)

    def display(self):
        print(f"{self.name} earns {self.salary}")


# Example usage:
e1 = Employee("Taswi", 50000)
e2 = Employee("Ravi", 40000)

print(e1)
print(e2)
print(e1 + e2)
print(len(e1))
e1.display()