input = list(map(int, open("input.txt").read().split(",")))

def simulate(days):
    age_limit = 8
    fishes = list(map(lambda age: input.count(age), range(age_limit+1)))
    for day in range(days):
        fishes_0 = fishes[0]
        fishes[0] = 0
        for age in range(1, (age_limit+1)):
            fishes[age-1] += fishes[age]
            fishes[age] = 0
        fishes[8] += fishes_0
        fishes[6] += fishes_0
    return sum(fishes)

print("Part 1: %d" % simulate(80))
print("Part 2: %d" % simulate(256))
