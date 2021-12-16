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

class System:
    def __init__(self):
        self.version_sum = 0

    def evalulate_packet(self, buffer):
        version = buffer.read_bits(3)
        type_id = buffer.read_bits(3)
        print("Packet header: %d, %d" % (version, type_id))
        self.version_sum += version

        if type_id == 4: # literal
            value = 0
            reading_value_groups = 1
            while reading_value_groups:
                reading_value_groups = buffer.read_bits(1)
                value = ((value<<4)+buffer.read_bits(4))
            print("Literal value: %d" % value)
            return value
        else: # operator
            op_args = []
            length_type_id = buffer.read_bits(1)
            if length_type_id == 0:
                packet_start_offset = buffer.bit_offset
                bits_remaining = buffer.read_bits(15)
                while bits_remaining > 0:
                    op_args.append(self.evalulate_packet(buffer))
                    bits_remaining -= (buffer.bit_offset-packet_start_offset)
            else:
                packet_count = buffer.read_bits(11)
                op_args += [self.evalulate_packet(buffer) for i in range(packet_count)]

        return 0

system = System()
result = system.evalulate_packet(Buffer(open("input.txt").read()))
print("Part 1: %d" % system.version_sum)
print("Part 2: %d" % result)
