input = list(map(int, open("input.txt", "r").read().splitlines()))

answer = sum([int(i > 0 and input[i]) > input[i-1] for i in range(len(input))])

print(answer)