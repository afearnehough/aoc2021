

class Buffer:
    def __init__(self, hex_string):
        self.bit_offset = 0
        self.bytes = bytes.fromhex((hex_string+'0') if (len(hex_string)%2) else hex_string)

    def read(self, bit_count):
        return self.read_bits(bit_count)

    def read_bits(self, bit_count):
        for bit in range(self.bit_offset, (self.bit_offset+bit_count)):
            yield ((self.bytes[bit>>3]>>(7-(bit&7)))&1)
        self.bit_offset += bit_count

class BITS:
    def __init__(self):
        self.packets = []

    def process_transmission(self, transmission):
        buffer = Buffer(transmission)
        print("".join(map(str, buffer.read(len(transmission)*4))))

BITS().process_transmission(open("input.txt").read())

# 00111000000000000110111101000101001010010001001000000000
# 00111000000000000110111101000101001010010001001000000000