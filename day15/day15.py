import heapq

class Cave:
    def __init__(self, cells):
        self.cells = cells
        self.size = (len(cells[0]), len(cells))

    def cell(self, x, y):
        if x < 0 or y < 0 or x >= (cave.size[0]*5) or y >= (cave.size[1]*5): return 9
        rx,ry = int(x/self.size[0]), int(y/self.size[0])
        value = self.cells[y%self.size[1]][x%self.size[0]]
        return ((value+(rx+ry-1))%9+1) if (rx+ry) > 0 else value

    def find(self, sx, sy, gx, gy):
        # Dijkstra yadda yadda...
        queue = []
        risks = {(sx, sx):0}
        heapq.heappush(queue, (0, (sx, sy)))
        while len(queue):
            x, y = heapq.heappop(queue)[1]
            if (x == gx and y == gy):
                return risks[(gx, gy)]
            else:
                for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    ax, ay = (x+dx), (y+dy)
                    risk = (risks[(x, y)]+self.cell(ax, ay))
                    if (ax, ay) not in risks or risk < risks[(ax, ay)]:
                        risks[(ax, ay)] = risk
                        heapq.heappush(queue, (risk, (ax, ay)))
        return False

cave = Cave([[int(cell) for cell in row] for row in open("input.txt").read().splitlines()])

print("Part 1: %d" % cave.find(0, 0, (cave.size[0]-1), (cave.size[1]-1)))
print("Part 2: %d" % cave.find(0, 0, (cave.size[0]*5-1), (cave.size[1]*5-1)))