# python3
import collections

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # make a list of list called elims
        self.elems = [collections.deque() for _ in range(bucket_count)]
        self.printlist = []

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return (ans % self.bucket_count)-1


    def read_query(self):
        return Query(input().split())

    def process_query(self, query):

        if query.type == 'check':
            self.printlist.append(list(self.elems[query.ind-1]))

        else:
            current_hash = self._hash_func(query.s)

            if query.type == "add":
                if query.s in self.elems[current_hash]:
                    pass
                else:
                    self.elems[current_hash].appendleft(query.s)

            if query.type == "del":
                try:
                    self.elems[current_hash].remove(query.s)
                except:
                    pass

            if query.type == "find":
                if query.s in self.elems[current_hash]:
                    self.printlist.append("yes")
                else:
                    self.printlist.append("no")


    def process_queries(self):
        n = int(input())

        for i in range(n):
            self.process_query(self.read_query())

        for elem in self.printlist:
            if type(elem) == list:
                print(' '.join(elem))
            else:
                print(elem)


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)

    proc.process_queries()
