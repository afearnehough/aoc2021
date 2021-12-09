

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
            "abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg",
        ]))

        for i in range(2): # 2 iterations
            for pattern in patterns:
                compatible = list(filter(lambda number: len(number) == len(pattern), self.n_map))
                if len(compatible) == 1:
                    compatible = compatible[0]
                    for d_key in self.d_map.keys():
                        self.d_map[d_key] = list(filter(lambda seg_v: seg_v in compatible if d_key in pattern else seg_v not in compatible, self.d_map[d_key]))

        # for segment, possible in self.d_map.items():
        #     if len(possible) == 2:
        #         if possible[0] == 'c' and possible[1] == 'f':
        #             self.d_map[segment] = ['c'] if 'c' in self.n_map[2]:

        #             else:

        # for segment, possible in self.d_map.items():
        #     print(segment, possible)



##-----------------------------------------------------------------------------------------------##

display = Display()

input = open("input.txt", "r").read().splitlines()
for entry in input:
    decoder = Decoder(entry.split("|")[0].split())
    break


display.set_digit(0, "acdeg")
display.set_digit(1, "cf")
display.set_digit(2, "abdfg")
display.set_digit(3, "abdefg")
display.display()
