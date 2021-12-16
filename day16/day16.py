class Buffer:
    def __init__(self, hex_string):
        self.bit_offset = 0
        self.bytes = bytes.fromhex(hex_string)
        self.length = len(self.bytes)

    def read_bits(self, count):
        result, result_offset = 0, 0
        for bit in range(self.bit_offset, (self.bit_offset+count)):
            if ((self.bytes[bit>>3]>>((7-bit)&7))&1):
                result |= (1<<(count-1-result_offset))
            result_offset += 1
        self.bit_offset += count
        return result

class System:
    def __init__(self):
        self.version_sum = 0

    def evalulate_packet(self, buffer):
        version = buffer.read_bits(3)
        type_id = buffer.read_bits(3)
        self.version_sum += version

        if type_id == 4: # literal
            value = 0
            reading_value_groups = 1
            while reading_value_groups:
                reading_value_groups = buffer.read_bits(1)
                value = ((value<<4)+buffer.read_bits(4))
            return value
        else: # operator
            arguments = []
            length_type_id = buffer.read_bits(1)
            if length_type_id == 1:
                packet_count = buffer.read_bits(11)
                arguments += [self.evalulate_packet(buffer) for i in range(packet_count)]
            else:
                bits_remaining = buffer.read_bits(15)
                packet_start_offset = buffer.bit_offset
                while bits_remaining > 0:
                    arguments.append(self.evalulate_packet(buffer))
                    bits_remaining -= (buffer.bit_offset-packet_start_offset)
            return 0

system = System()
result = system.evalulate_packet(Buffer(open("input.txt").read()))
print("Part 1: %d" % system.version_sum)
print("Part 2: %d" % result)

# 01100010000000001000000000000000000101100001000101010110001011001000100000000010000100011000111000110100

# 011 000 1 00000000010 | 000 000 0 000000000010110 | 000 100 0 1010 | 101 100 0 1011 | 001 000 1 00000000010 | 000 100 0 1100 | 011 100 0 1101 | 00
# VVV TTT I LLLLLLLLLLL | VVV TTT I LLLLLLLLLLLLLLL | VVV TTT G NNNN | VVV TTT G NNNN | VVV TTT I LLLLLLLLLLL | VVV TTT G NNNN | VVV TTT G NNNN |
#   3   0 1           2 |   0   0 0              22 |   0   4 0   10 |   5   4 0   11 |   1   0 1           2 |   0   4 0   12 |   3   4 0   13 |

# remaining: 20
# start: 5
# current 10
# remaining: 20-(10-5)