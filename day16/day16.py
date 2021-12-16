class Buffer:
    def __init__(self, hex_string):
        self.bit_offset = 0
        self.bytes = bytes.fromhex((hex_string+'0') if (len(hex_string)%2) else hex_string)
        self.length = len(self.bytes)

    def read_bits(self, count):
        result, result_offset = 0, 0
        for bit in range(self.bit_offset, (self.bit_offset+count)):
            if ((self.bytes[bit>>3]>>((7-bit)&7))&1):
                result |= (1<<(count-1-result_offset))
            result_offset += 1
        self.bit_offset += count
        return result

class BITS:
    def __init__(self):
        self.packets = []

    def process_transmission(self, transmission):
        buffer = Buffer(transmission)


        print(buffer.read_bits(3))
        print(buffer.read_bits(3))
        print(buffer.read_bits(1))
        print(buffer.read_bits(15))

BITS().process_transmission(open("input.txt").read())

# 00111000000000000110111101000101001010010001001000000000
# 00111000000000000110111101000101001010010001001000000000
