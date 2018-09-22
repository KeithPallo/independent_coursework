# python3

class phone_book:
    def __init__(self,actions):
        self.actions = actions
        self.book = {}
        self.output = []

    def make_book(self):
        for i in range(len(self.actions)):

            current = self.actions[i]

            if current.type == "add":
                self.book[current.number] = current.name

            if current.type == "find":
                x = self.book.get(current.number)

                if x == None:
                    self.output.append("not found")
                else:
                    self.output.append(x)

            if current.type == "del":
                try:
                    del self.book[current.number]
                except:
                    continue



    def print_special(self):
        for i in range(len(self.output)):
            print(self.output[i])




class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):

    return

def process_queries(queries):

    x = phone_book(queries)

    x.make_book()
    x.print_special()


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

