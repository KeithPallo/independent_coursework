#!/usr/bin/python3


import sys, threading

sys.setrecursionlimit(10 ** 9)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        self.result = []
        self.final = True
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self, x=0):

        #print(self.final)
        # Check if false condition already
        if self.final == False:
            return

        # Check if left node
        if self.left[x] != -1:

            # Check to see if the right child has a left node

            if self.left[self.left[x]] != -1:

                if self.key[self.left[self.left[x]]] == self.key[x]:
                    self.final = False
                    return


            if self.right[self.left[x]] != -1:

                if self.left[self.left[x]] != -1:

                   if self.key[self.left[self.left[x]]] == self.key[x]:
                    self.final = False
                    return

                # If the right child of the left node is equal to or great than the current key, initiate False
                if self.key[self.right[self.left[x]]] >= self.key[x]:
                    self.final = False
                    return


                else:
                    if self.key[self.left[x]] < self.key[x]:
                        self.inOrder(self.left[x])
                    else:
                        self.final = False
                        return


            else:
                if self.key[self.left[x]] < self.key[x]:
                    self.inOrder(self.left[x])
                else:
                    self.final = False
                    return

        # Append the current node if there is no left node
        self.result.append(self.key[x])

        # Check if there is a right node
        if self.right[x] != -1:

            # Check if the right node is at least the current node
            if self.key[self.right[x]] >= self.key[x]:


                # If it is, then check to see if the right node has a left child
                if self.left[self.right[x]] != -1:

                    # If the left child of the right node is equal to the current key, initiate False
                    if self.key[self.left[self.right[x]]] < self.key[x]:
                        self.final = False
                        return

                    else:
                        # Recursive call
                        self.inOrder(self.right[x])
                else:
                    # Recursive call for no special function
                    self.inOrder(self.right[x])
                


            elif self.key[self.right[x]] < self.key[x]:
                self.final = False
                return

            else:
                if len(self.result) == self.n:
                    return



def main():

    tree = TreeOrders()
    tree.read()
    if tree.n == 0:
      print("CORRECT")
      return

    tree.inOrder()

    result = tree.final


    if result == True:

      print("CORRECT")

    else:
      print("INCORRECT")


threading.Thread(target=main).start()
