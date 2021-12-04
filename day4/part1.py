import math

class Board:
    def __init__(self, numbers, width, height):
        self.width = width
        self.height = height
        self.numbers = numbers
        self.reset()

    def check_and_mark(self, number):
        if number in self.numbers:
            index = self.numbers.index(number)
            self.marked[index] = True
            # do we have a winner?
            x = math.floor(index/self.width)
            y = index%self.height
            if self.check_full_col(y) or self.check_full_row(x):
                return True
        return False

    def check_full_row(self, y):
        for x in range(self.width):
            if not self.marked[x+y*self.width]:
                return False
        return True

    def check_full_col(self, x):
        for y in range(self.height):
            if not self.marked[x+y*self.height]:
                return False
        return True

    def calculate_score(self):
        return sum(list(map(lambda it: it[1] if not self.marked[it[0]] else 0, enumerate(self.numbers))))

    def print_marked(self):
        for y in range(self.height):
            for x in range(self.width):
                print(int(self.marked[x+y*self.width]), end='')
            print()

    def reset(self):
        self.marked = [False]*len(numbers)

# read input
input = open("input.txt", "r").read().split("\n\n")
numbers = list(map(int, input[0].split(",")))
boards = list(map(lambda numbers: Board(list(map(int, numbers.split())), 5, 5), input[1:]))

# process numbers
def part1():
    for number in numbers:
        for board in boards:
            if board.check_and_mark(number):
                print(board.calculate_score()*number)
                return
    print("No winners?")

part1()
