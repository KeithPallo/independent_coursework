# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def __str__(self):
        return str(self.bracket_type) + "" + str(self.position)

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()
    check = 0
    opening_brackets_stack = []
    for i, next in enumerate(text):

        if next == '(' or next == '[' or next == '{':

            opening_brackets_stack.append(Bracket(next,i))


        if next == ')' or next == ']' or next == '}':

            if len(opening_brackets_stack) == 0:
                print(i+1)
                sys.exit()
                check = 1
                break

            test = Bracket(next,i)
            last = opening_brackets_stack[-1]

            if last.Match(test.bracket_type) == True:
                opening_brackets_stack.pop()


            else:
                print(i+1)
                sys.exit()
                check = 1




    if len(opening_brackets_stack) == 0 and check == 0:
        print("Success")

    else:
        wrong = opening_brackets_stack[0]
        print((wrong.position + 1))