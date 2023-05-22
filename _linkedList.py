class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_front(self, data):
        self.head = Node(data, self.head)

    def add_end(self, data):
        if not self.head:
            self.head = Node(data, None)
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = Node(data, None)

    def get_last_node(self):
        h = self.head
        while h.next != None:
            h = h.next
        return h.data

    def is_empty(self):
        return self.head == None

    def print_linked_list(self):
        h = self.head
        while h.next != None:
            print(h.data, end=" ")
            h = h.next
        print("")

# Example


l = LinkedList()

print("Linked List is emty: ", l.is_empty())
# Linked List is emty:  True

l.add_front(5)
l.add_front(4)
l.add_front(2)

l.add_end(0)
l.add_end(1)
l.add_end(-1)

l.print_linked_list()
# 2 4 5 0 1

print("The last node is ", l.get_last_node())
# The last node is  -1

print("Linked List is emty: ", l.is_empty())
# Linked List is emty:  False
