from collections import defaultdict

input = open("input.txt").read().split("\n\n")
rules = defaultdict(str)
for rule in [entry.split(" -> ") for entry in input[1].splitlines()]:
    rules[rule[0]] = rule[1]

def calculate(elems, steps):
    counts = defaultdict(int)
    for elem in elems:
        counts[elem] += 1
        
    pairs = defaultdict(int)
    for pair in [elems[i:i+2] for i in range(len(elems)-1)]:
        pairs[pair] += 1

    for step in range(steps):
        new_pairs = defaultdict(int)
        for pair, count in pairs.items():
            counts[rules[pair]] += count
            new_pairs[pair[0]+rules[pair]] += count
            new_pairs[rules[pair]+pair[1]] += count
        pairs = new_pairs
    counts = list(sorted(counts.items(), key=lambda it: it[1]))
    return (counts[-1][1]-counts[0][1])

print("Part 1: %s" % calculate(input[0], 10))
print("Part 2: %s" % calculate(input[0], 40))
