input = open("input.txt", "r").read().splitlines()

def str_sort(string):
    return "".join(sorted(string))

def str_common(string1, string2):
    return len(set(string1).intersection(string2))

class Decoder:
    def __init__(self, patterns):
        self.patterns = patterns

        self.mapping = ([None]*10)
        self.numbers = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]

        self.mapping[1] = str_sort(self.get_patterns_of_length(2)[0])
        self.mapping[7] = str_sort(self.get_patterns_of_length(3)[0])
        self.mapping[4] = str_sort(self.get_patterns_of_length(4)[0])
        self.mapping[8] = str_sort(self.get_patterns_of_length(7)[0])

        for pattern in [str_sort(pattern) for pattern in patterns]:
            length = len(pattern)
            if length == 5:
                if str_common(self.mapping[4], pattern) == 2:
                    self.mapping[2] = pattern
                elif str_common(self.mapping[4], pattern) == 3:
                    if str_common(self.mapping[1], pattern) == 2:
                        self.mapping[3] = pattern
                    else:
                        self.mapping[5] = pattern
            elif length == 6:
                if str_common(self.mapping[1], pattern) == 2:
                    if str_common(self.mapping[4], pattern) == 4:
                        self.mapping[9] = pattern
                    else:
                        self.mapping[0] = pattern
                else:
                    self.mapping[6] = pattern

    def decode(self, values):
        return [self.mapping.index(value) for value in [str_sort(value) for value in values]]
        
    def get_patterns_of_length(self, length):
        return list(filter(lambda pattern: len(pattern) == length, self.patterns))


uniques = 0
total = 0
for entry in input:
    (patterns, output) = entry.split("|")
    decoder = Decoder(patterns.split())
    result = decoder.decode(output.split())
    uniques += sum([value in [1, 4, 7, 8] for value in result])
    total += int("".join(map(str, result)))

print("Part 1: %d" % uniques)
print("Part 2: %d" % total)
