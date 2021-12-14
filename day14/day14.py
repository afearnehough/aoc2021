from collections import defaultdict

def calculate(elems, steps):
    for step in range(steps):
        result = ""
        for i in range(len(elems)-1):
            result += (elems[i]+rules[elems[i:i+2]])
        elems = (result+elems[-1])
    return elems

input = open("input.txt").read().split("\n\n")
rules = defaultdict(str)
for rule in [entry.split(" -> ") for entry in input[1].splitlines()]:
    rules[rule[0]] = rule[1]
elems = calculate(input[0], 10)
count = sorted([(elem, elems.count(elem)) for elem in set(elems)], key=lambda it: it[0])

print("Part 1: %d" % (count[0][1]-count[-1][1]))
