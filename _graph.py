class Graph:
    def __init__(self, size):
        self.adj = [[0]*size for i in range(size)]
        self.size = size

    def add_edge(self, orig, dest):
        if orig > self.size or dest > self.size or orig < 0 or dest < 0:
            print("Invalided Edge")
        else:
            self.adj[orig-1][dest-1] = 1
            self.adj[dest-1][orig-1] = 1

    def remove_edge(self, orig, dest):
        if orig > self.size or dest > self.size or orig < 0 or dest < 0:
            print("Invalided Edge")
        else:
            self.adj[orig-1][dest-1] = 0
            self.adj[dest-1][orig-1] = 0

    def display(self):
        for row in self.adj:
            print()
            for i in row:
                print('{:4}'.format(i), end=" ")
        print("")

# Example


g = Graph(5)
for i in range(6):
    g.add_edge(i, i)

g.display()

print("_____"*5)


for i in range(1, 6):
    g.remove_edge(i, i)
g.display()

""" 
   1    0    0    0    0
   0    1    0    0    0
   0    0    1    0    0
   0    0    0    1    0
   0    0    0    0    1
_________________________

   0    0    0    0    0
   0    0    0    0    0
   0    0    0    0    0
   0    0    0    0    0
   0    0    0    0    0
"""
