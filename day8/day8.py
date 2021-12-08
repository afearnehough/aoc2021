

class Display:
    def __init__(self, digit_count=4):
        self.digit_width = 6
        self.digit_height = 7
        self.digit_count = digit_count
        self.digit_image = [0,1,1,1,1,0,2,0,0,0,0,3,2,0,0,0,0,3,0,4,4,4,4,0,5,0,0,0,0,6,5,0,0,0,0,6,0,7,7,7,7,0]
        self.width = (self.digit_width*self.digit_count+digit_count)
        self.pixels = (([' ']*(self.width*self.digit_height)))
        self.segments = "abcdefg"
        self.clear()

    def clear(self):
        for digit_index in range(self.digit_count):
            self.set_digit(digit_index, "")

    def set_digit(self, digit_index, segments):
        if 0 <= digit_index < self.digit_count:
            for y in range(self.digit_height):
                for x in range(self.digit_width):
                    value = (self.digit_image[x+y*self.digit_width])
                    pixel = ((digit_index*(self.digit_width+1)+x)+y*self.width)
                    self.pixels[pixel] = ' '
                    if value > 0:
                        self.pixels[pixel] = self.segments[value-1] if self.segments[value-1] in segments else '.'

    def display(self):
        for y in range(self.digit_height):
            print("".join(self.pixels[(y*self.width):((y*self.width)+self.width)]))

##-----------------------------------------------------------------------------------------------##

class Decoder:
    def __init__(self, patterns):
        self.d_map = dict.fromkeys([x for x in "abcdefg"], [x for x in "abcdefg"])
        self.n_map = list(map(lambda number: [segment for segment in number], [
            "abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"
        ]))

        def is_compatible(pattern, number):
            if len(number) != len(pattern):
                return False
            for seg_i in pattern:
                for seg_j in number:
                    if seg_j not in self.d_map[seg_i]:
                        print("%s: %s not in %s"  % ("".join(number), seg_j, "".join(self.d_map[seg_i])))
                        return False
            return True

        for pattern in patterns:
            compatible = list(filter(lambda number: is_compatible(pattern, number), self.n_map))

            print()
            print(pattern, compatible)
            for k, v in self.d_map.items():
                print(k, v)

            if len(compatible) == 1:
                compatible = compatible[0]
                for d_key in self.d_map.keys():
                    if d_key not in pattern:
                        self.d_map[d_key] = list(filter(lambda seg_v: seg_v not in compatible, self.d_map[d_key]))
                    else:
                        self.d_map[d_key] = list(filter(lambda seg_v: seg_v in compatible, self.d_map[d_key]))


##-----------------------------------------------------------------------------------------------##

display = Display()
decoder = Decoder("be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb".split())
display.set_digit(0, "abcdefg")
display.display()
