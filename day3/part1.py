diagnostic_data = open("input.txt", "r").read().splitlines()

sums = [0]*len(diagnostic_data[0])
for line in diagnostic_data:
    for bit in range(len(line)):
        sums[bit] += int(line[bit])

common = [int(value > len(diagnostic_data)/2) for value in reversed(sums)]
to_dec = lambda bits: sum([bits[bit]*(2**bit) for bit in range(len(bits))])
gamma = to_dec(common)
epsilon = to_dec([not bit for bit in common])

print(common)
print(gamma)
print(epsilon)
print(gamma*epsilon)
