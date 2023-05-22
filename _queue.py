class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def print_queue(self):
        print(self.items)


q = Queue()

print(q.is_empty())
# True

q.enqueue('3')
q.enqueue('N')
q.enqueue('O')
q.enqueue('H')
q.enqueue('T')
q.enqueue('Y')
q.enqueue('P')

q.print_queue()
# ['P', 'Y', 'T', 'H', 'O', 'N', '3']

q.dequeue()
# Delete '3'

q.print_queue()
# ['P', 'Y', 'T', 'H', 'O', 'N']

print(q.is_empty())
# False
