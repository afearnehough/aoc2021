import math

class Mapper:
    def __init__(self, segments):
        self.segments = segments # list of segment tuples containing coordinate tuples
        self.width = (max(list(map(lambda segment: max(segment[0][0], segment[1][0]), segments)))+1)
        self.height = (max(list(map(lambda segment: max(segment[0][1], segment[1][1]), segments)))+1)
        self.area = (self.width*self.height)
        self.reset()

    def reset(self):
        self.values = ([0]*self.area)

    def plot_segments(self, filter_func = lambda seg: True):
        for segment in self.segments:
            if filter_func(segment):
                # DDA https://en.wikipedia.org/wiki/Digital_differential_analyzer_(graphics_algorithm)
                x0, y0 = segment[0]
                x1, y1 = segment[1]
                dx, dy = (x1-x0), (y1-y0)
                ax, ay = abs(dx), abs(dy)
                step = ax if ax >= ay else ay
                dx, dy = (dx/step), (dy/step)
                cx, cy = x0, y0
                for i in range(0, (step+1)):
                    self.values[int(cx)+int(cy)*self.width] += 1
                    cx, cy = (cx+dx), (cy+dy)

    def count_overlaps(self, threshold):
        return sum(list(map(lambda value: 1 if value >= threshold else 0, self.values)))

    def draw(self):
        for y in range(self.height):
            for x in range(self.width):
                value = self.values[x+y*self.width]
                print('.' if value == 0 else value, end='')
            print()

class Input:
    def __init__(self):
        self.segments = list(map(self.parse_segment, open("input.txt").read().splitlines()))

    def parse_coord(self, coord):
        return tuple(map(int, coord.split(",")))

    def parse_segment(self, line):
        return (self.parse_coord(line.split()[0]), self.parse_coord(line.split()[2]))


input = Input()
mapper = Mapper(input.segments)
mapper.plot_segments(lambda seg: seg[0][0] == seg[1][0] or seg[0][1] == seg[1][1])
print("Part 1: %d" % mapper.count_overlaps(2))
mapper.reset()
mapper.plot_segments()
print("Part 2: %d" % mapper.count_overlaps(2))
