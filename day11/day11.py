data = [int(energy) for energy in open("input.txt").read().replace("\n", "")]
length = 10

def display():
    print()
    for y in range(length):
        for x in range(length):
            print(data[x+y*length], end='')
        print()

def step():
    stack = []
    flashes = 0

    def charge(x, y):
        index = (x+y*length)
        data[index] += 1
        if data[index] > 9:
            data[index] = 0
            stack.append((x, y))
            nonlocal flashes
            flashes += 1

    for y in range(length):
        for x in range(length):
            charge(x, y)
    while len(stack):
        (x, y) = stack.pop()
        for (dx, dy) in [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]:
            ax, ay = (x+dx), (y+dy)
            if 0 <= ax < length and 0 <= ay < length:
                if data[(ax+ay*length)] != 0:
                    charge(ax, ay)

    return flashes


print("Part 1: %d" % sum([step() for i in range(100)]))
step_count = 100
while step() != (length*length):
    step_count += 1
print("Part 2: %d" % (step_count+1))




