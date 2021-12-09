
data = list(map(lambda heights: [int(height) for height in heights], open("input.txt", "r").read().splitlines()))
size = (len(data[0]), len(data))

def cell(x, y, default=9):
    return data[y][x] if 0 <= x < size[0] and 0 <= y < size[1] else default

risk_sum = 0
basins = []
cells_visited = {}

for y in range(size[1]):
    for x in range(size[0]):
        if all(cell(x, y) < height for height in [cell((x+1), y), cell((x-1), y), cell(x, (y-1)), cell(x, (y+1))]):
            risk_sum += (cell(x, y)+1)
            basin_size = 0
            basin_search_stack = [(x, y)]

            while len(basin_search_stack):
                (sx, sy) = basin_search_stack.pop()
                cell_height = cell(sx, sy)
                if cell_height < 9:
                    data[sy][sx] = 9
                    basin_size += 1
                    basin_search_stack += [((sx+1), sy), ((sx-1), sy), (sx, (sy+1)), (sx, (sy-1))]

            basins.append(basin_size)

print(risk_sum)
print(basins)
basins = sorted(basins)[-3:]
print(basins[0]*basins[1]*basins[2])
