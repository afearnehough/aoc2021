diagnostic_data = list(map(lambda line: list(map(lambda bit: int(bit), line)), open("input.txt", "r").read().splitlines()))
to_dec = lambda bits: sum([bits[len(bits)-bit-1]*(2**bit) for bit in range(len(bits))])

def calculate(data, invert):
    line_width = len(data[0])
    for bit_i in range(line_width):
        bit_sum = sum([line[bit_i] for line in data])
        bit_common = int(bit_sum >= (len(data)-bit_sum))
        if len(data) > 1:
            data = filter(lambda line: line[bit_i] == (bit_common^invert), data)
        else: break
    return data


ogr = to_dec(calculate(diagnostic_data, 0)[0])
csr = to_dec(calculate(diagnostic_data, 1)[0])
print(ogr*csr)
