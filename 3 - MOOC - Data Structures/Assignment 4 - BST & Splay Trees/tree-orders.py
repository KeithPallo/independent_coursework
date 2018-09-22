# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    self.result = []
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self,x=0):

    if self.left[x] != -1:
        self.inOrder(self.left[x])

    self.result.append(self.key[x])

    if self.right[x] != -1:
        self.inOrder(self.right[x])

    if len(self.result) == self.n:
        print(*self.result, sep = " ")
        self.result.clear()

  def preOrder(self, x=0):

    self.result.append(self.key[x])

    if self.left[x] != -1:
        self.preOrder(self.left[x])

    if self.right[x] != -1:
        self.preOrder(self.right[x])

    if len(self.result) == self.n:
        print(*self.result, sep=" ")
        self.result.clear()


  def postOrder(self, x=0):



    if self.left[x] != -1:
        self.postOrder(self.left[x])

    if self.right[x] != -1:
        self.postOrder(self.right[x])

    self.result.append(self.key[x])

    if len(self.result) == self.n:
        print(*self.result, sep=" ")
        self.result.clear()


def main():
    tree = TreeOrders()
    tree.read()
    tree.inOrder()
    tree.preOrder()
    tree.postOrder()

threading.Thread(target=main).start()
