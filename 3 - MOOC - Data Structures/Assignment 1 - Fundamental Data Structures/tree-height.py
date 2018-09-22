# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return self.items


class Node:

    def __init__(self,index):
        self.parent = False
        self.leaf = False
        self.children = []
        self.height = 0
        self.index = index

    def add_child(self,child_index):
        self.children.append(child_index)



class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                self.root = False
                self.height = 0
                self.nodes = []
                self.stack = Stack()



        def make_nodes(self):
               for vertex in range(self.n):
                    self.nodes.append(Node(self.parent[vertex]))



        def add_children(self):
                for vertex in range(self.n):
                        i = vertex
                        if self.parent[i] == -1:
                            self.root = i
                        else:
                            self.nodes[self.parent[i]].add_child(i)



        def node_height(self,index):
            self.stack.push(index)

            if len(self.nodes[index].children) == 0:
                if self.stack.size() > self.height:
                    self.height = self.stack.size()

            else:
                for i in range(len(self.nodes[index].children)):
                    current_child = self.nodes[index].children[i]

                    if len(self.nodes[current_child].children) == 0:
                        if self.stack.size() > self.height:
                            self.height = self.stack.size()

                    else:
                        self.node_height(current_child)

            self.stack.pop()



def main():
  tree = TreeHeight()
  tree.read()
  tree.make_nodes()
  tree.add_children()
  tree.node_height(tree.root)
  print(tree.height+1)

threading.Thread(target=main).start()
