import heapq

class Cave:
    def __init__(self, cells):
        self.cells = cells
        self.size = (len(cells[0]), len(cells))

    def cell(self, x, y):
        rx,ry = int(x/self.size[0]), int(y/self.size[0])
        value = self.cells[y%self.size[1]][x%self.size[0]]
        return ((value+(rx-1))%9+1) if rx > 0 else value

    def find(self, sx, sy, gx, gy):
        # A* yadda yadda...
        queue = []
        costs = {(sx, sx):0}
        heapq.heappush(queue, (0, (sx, sy)))
        while len(queue):
            x, y = heapq.heappop(queue)[1]
            if (x == gx and y == gy):
                return costs[(gx, gy)]
            else:
                for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    ax, ay = (x+dx), (y+dy)
                    cost_to_move = (costs[(x, y)]+self.cell(ax, ay))
                    if (ax, ay) not in costs or cost_to_move < costs[(ax, ay)]:
                        costs[(ax, ay)] = cost_to_move
                        heapq.heappush(queue, ((cost_to_move+(abs(gx-ax)+abs(gy-ay))), (ax, ay)))
        return False

cave = Cave([[int(cell) for cell in row] for row in open("input.txt").read().splitlines()])

# print("Part 1: %d" % cave.find(0, 0, (cave.size[0]-1), (cave.size[1]-1)))

for i in range(5):
    print(",", end='')
    for c in range(10):
        print(cave.cell(i*10+c, 0), end='')