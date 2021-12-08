class Decoder:
    def __init__(self, signal_patterns):
        pass
class Display:
    def __init__(self, digit_count=4, digit_width=6, digit_height=7):
        self.digit_width = digit_width
        self.digit_height = digit_height
        self.digit_count = digit_count
        self.width = (digit_width*digit_count+digit_count)
        self.pixels = ((['.']*(self.width*digit_height)))

    def display(self):
        for y in range(self.digit_height):
            print("".join(self.pixels[(y*self.width):((y*self.width)+self.width)]))

decoder = Decoder()
display = Display()
display.set_value(1234)
display.display()

# display.process_signal_patterns("be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb".split())
