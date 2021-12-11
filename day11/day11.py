data = [int(energy) for energy in open("input.txt").read().replace("\n", "")]
length = 10

def display():
    print()
    for y in range(length):
        for x in range(length):
            print(data[x+y*length], end='')
        print()

flashes = 0

for step in range(0, 100):
    stack = []

    def charge(x, y):
        index = (x+y*length)
        data[index] += 1
        if data[index] > 9:
            data[index] = 0
            stack.append((x, y))
            global flashes
            flashes += 1

    for y in range(length):
        for x in range(length):
            index = (x+y*length)
            charge(x, y)
    while len(stack):
        (x, y) = stack.pop()
        for (dx, dy) in [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]:
            ax, ay = (x+dx), (y+dy)
            if 0 <= ax < length and 0 <= ay < length:
                if data[(ax+ay*length)] != 0:
                    charge(ax, ay)

print("Part 1: %d" % flashes)
