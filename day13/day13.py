

def draw(coords):
    if len(coords):
        sizex = (max([coord[0] for coord in coords])+1)
        sizey = (max([coord[1] for coord in coords])+1)
        paper = (['.']*(sizex*sizey))
        for coord in coords:
            paper[coord[0]+coord[1]*sizex] = "#"
        print()
        for y in range(sizey):
            for x in range(sizex):
                print(paper[x+y*sizex], end="")
            print()


def fold(coords, folds, times):
    rline = folds.pop()
    print(rline)
    new_coords = []
    for coord in coords:
        x, y = coord
        i, j = rline
        new_coords.append((0, 0) if x > i and y > j else coord)
            # ((x, y-(y-j)*2))

    return fold(new_coords, folds, (times-1)) if times > 1 else new_coords

input = open("input.txt").read().split("\n\n")
coords = [(int(x), int(y)) for x, y in [line.split(",") for line in input[0].splitlines()]]
folds = list(reversed([fold.split()[2].split("=") for fold in input[1].splitlines()]))
folds = [(int(fold[1]), 0) if fold[0] == "x" else (0, int(fold[1])) for fold in folds]
draw(coords)
draw(fold(coords, folds, 1))
