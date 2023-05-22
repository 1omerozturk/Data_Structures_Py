class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def print_stack(self):
        print(self.items)


# Example
a = Stack()


print(a.is_empty())
# True

a.push("r")
a.push("e")
a.push("m")
a.push("o")
a.push("a")


a.print_stack()
# ['a', 'o', 'm', 'e', 'r']

a.pop()
# delete 'a'

a.print_stack()
# ['o', 'm', 'e', 'r']

print(a.is_empty())
# False
