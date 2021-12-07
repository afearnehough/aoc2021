crabs = list(map(int, open("input.txt").read().split(",")))

print("Part 1: %d" % min([sum([abs(x-tx) for x in crabs]) for tx in range(len(crabs))]))
print("Part 2: %d" % min([sum([ (abs(x-tx)*(abs(x-tx)+1)/2) for x in crabs]) for tx in range(len(crabs))]))
