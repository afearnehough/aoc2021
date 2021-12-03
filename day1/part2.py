input = list(map(int, open("input.txt", "r").read().splitlines()))

sums = [sum(input[i:i+3]) for i in range(len(input)-2)]

answer = sum([int(i > 0 and sums[i]) > sums[i-1] for i in range(len(sums))])

print(answer)
