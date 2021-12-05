class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def subtract(self, point):
        return Point(self.x-point.x, self.y-point.y)

    def __str__(self):
        return "%d,%d" % (self.x, self.y)

class Map:
    def __init__(self):
        self.map = []

    def add_segment(self, a: Point, b: Point):
        print(b.subtract(a))

class Input:
    def __init__(self):
        self.segments = list(map(self.parse_segment, open("input.txt").read().splitlines()))

    def parse_segment_coords(self, coords):
        return tuple(map(int, coords.split(",")))

    def parse_segment(self, line):
        return (
            Point(*self.parse_segment_coords(line.split()[0])),
            Point(*self.parse_segment_coords(line.split()[2])))


input = Input()
map = Map()
for segment in input.segments:
    map.add_segment(*segment)
