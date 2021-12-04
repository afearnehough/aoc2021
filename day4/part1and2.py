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
                self.win_count += 1
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

    def reset(self):
        self.win_count = 0
        self.marked = [False]*len(numbers)

# read input
input = open("input.txt", "r").read().split("\n\n")
numbers = list(map(int, input[0].split(",")))
boards = list(map(lambda numbers: Board(list(map(int, numbers.split())), 5, 5), input[1:]))

# process parts
def part1():
    for number in numbers:
        for board in boards:
            if board.check_and_mark(number):
                return (board.calculate_score()*number)

def part2():
    for board in boards:
        board.reset()
    boards_won = 0
    for number in numbers:
        for board in boards:
            if board.check_and_mark(number):
                if board.win_count == 1:
                    boards_won += 1
                    if boards_won >= len(boards):
                        return (board.calculate_score()*number)

print("Part 1: %s" % part1())
print("Part 2: %s" % part2())
