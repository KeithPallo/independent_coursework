#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


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

    def inOrder(self, x=0):

        if self.left[x] != -1:
            self.inOrder(self.left[x])

        self.result.append(self.key[x])

        if self.right[x] != -1:
            self.inOrder(self.right[x])

        if len(self.result) == self.n:
            self.test = self.result



def main():
    tree = TreeOrders()
    tree.read()
    if tree.n == 0:
      print("CORRECT")
      return
    tree.inOrder()
    result = tree.test

    if (all(result[i] <= result[i + 1] for i in range(len(result) - 1))):
      print("CORRECT")

    else:
      print("INCORRECT")



threading.Thread(target=main).start()
