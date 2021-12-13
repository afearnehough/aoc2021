def draw(coords):
    if len(coords):
        sizex = (max([coord[0] for coord in coords])+1)
        sizey = (max([coord[1] for coord in coords])+1)
        paper = (['.']*(sizex*sizey))
        for coord in coords:
            if coord[0] >= 0 and coord[1] >= 0:
                paper[coord[0]+coord[1]*sizex] = "#"
        for y in range(sizey):
            for x in range(sizex):
                print(paper[x+y*sizex], end="")
            print()

def fold(coords, folds, times):
    rline = folds.pop()
    new_coords = []
    for coord in coords:
        x, y = coord
        if rline[0] == "y":
            new_coords.append((x, (y-(y-rline[1])*2)) if y > rline[1] else coord)
        else:
            new_coords.append(((x-(x-rline[1])*2), y) if x > rline[1] else coord)
    return fold(new_coords, folds, (times-1)) if times > 1 else new_coords

input = open("input.txt").read().split("\n\n")
coords = [(int(x), int(y)) for x, y in [line.split(",") for line in input[0].splitlines()]]
folds = list(reversed([fold.split()[2].split("=") for fold in input[1].splitlines()]))
folds = [(fold[0], int(fold[1])) for fold in folds]
print("Part 1: %d" % len(set(fold(coords, folds, 1))))
print("Part 2:")
draw(fold(coords, folds, len(folds)))
