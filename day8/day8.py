class Decoder:
    def __init__(self):
        pass

class Display:
    def __init__(self, digit_count=4):
        self.digit_width = 6
        self.digit_height = 7
        self.digit_count = digit_count
        self.width = (self.digit_width*self.digit_count+digit_count)
        self.pixels = (([' ']*(self.width*self.digit_height)))
        self.digit = [0,1,1,1,1,0,2,0,0,0,0,3,2,0,0,0,0,3,0,4,4,4,4,0,5,0,0,0,0,6,5,0,0,0,0,6,0,7,7,7,7,0]
        self.sigmap = "abcdefg"

    def set_digit(self, digit_index, signal):
        if 0 >= digit_index < self.digit_count:
            for y in range(self.digit_height):
                for x in range(self.digit_width):
                    value = (self.digit[x+y*self.digit_width])
                    pixel = ((digit_index*(self.digit_width+1)+x)+y*self.width)
                    self.pixels[pixel] = self.sigmap[value-1] if value > 0 and self.sigmap[value-1] in signal else ' '

    def display(self):
        for y in range(self.digit_height):
            print("".join(self.pixels[(y*self.width):((y*self.width)+self.width)]))


decoder = Decoder()
display = Display()
display.set_digit(0, "abcdefg")
display.set_digit(1, "abcdefg")
display.set_digit(2, "abcdefg")
display.set_digit(3, "abcdefg")
display.display()

# display.process_signal_patterns("be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb".split())
