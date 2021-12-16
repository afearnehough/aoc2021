from functools import reduce

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
        self.ops = {
            0: lambda args: reduce(lambda x, y: (x+y), args),
            1: lambda args: reduce(lambda x, y: (x*y), args),
            2: min,
            3: max,
            5: lambda args: 1 if args[0]  > args[1] else 0,
            6: lambda args: 1 if args[0]  < args[1] else 0,
            7: lambda args: 1 if args[0] == args[1] else 0
        }

    def evaluate_packet(self, buffer):
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
                arguments += [self.evaluate_packet(buffer) for i in range(packet_count)]
            else:
                bit_length = buffer.read_bits(15)
                packet_start_offset = buffer.bit_offset
                while (buffer.bit_offset-packet_start_offset) < bit_length:
                    arguments.append(self.evaluate_packet(buffer))
            return self.ops[type_id](arguments)

system = System()
result = system.evaluate_packet(Buffer(open("input.txt").read()))
print("Part 1: %d" % system.version_sum)
print("Part 2: %d" % result)
