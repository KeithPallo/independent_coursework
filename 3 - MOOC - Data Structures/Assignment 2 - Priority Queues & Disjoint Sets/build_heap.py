# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []
    self.size = False

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)
    self.size = n

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def sift_down(self,input_index):
    min_index = input_index
    lc = 2 * input_index

    if lc <= (self.size):
        if self._data[lc-1] < self._data[min_index-1]:
            min_index = lc

    rc = lc + 1

    if rc <= (self.size):
        if self._data[rc-1] < self._data[min_index-1]:
            min_index = rc

    if input_index != min_index:
        swap_account = [input_index-1,min_index-1]
        self._swaps.append(swap_account)

        self._data[input_index-1],self._data[min_index-1] = self._data[min_index-1], self._data[input_index-1]

        self.sift_down(min_index)



  def GenerateSwaps(self):


    for i in range(self.size // 2,0,-1):

        self.sift_down(i)



  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()

