from functools import reduce

class Parser:
    Openings = ['(', '[', '{', '<']
    Pairings = ["()", "[]", "{}", "<>"]
    Closings = [')', ']', '}', '>']

    ResultOk = 0
    ResultIncomplete = 1
    ResultError = 2

    def parse(self, tokens):
        stack = []
        for token in tokens:
            if token in self.Openings:
                stack.append(token)
            elif token in self.Closings:
                pairing = (stack[-1] + token)
                if pairing in self.Pairings:
                    stack.pop()
                else: return (self.ResultError, token)
        if len(stack):
            return (self.ResultIncomplete, list(reversed(list(map(lambda token: self.Closings[self.Openings.index(token)], stack)))))
        else:
            return (self.ResultOk, "")


input = open("input.txt").read().splitlines()
results = [Parser().parse(line) for line in input]

errors = list(filter(lambda result: result[0] == Parser.ResultError, results))
incoms = list(filter(lambda result: result[0] == Parser.ResultIncomplete, results))

p1_scores = [3, 57, 1197, 25137]
print("Part 1: %d" % sum(map(lambda result: p1_scores[Parser.Closings.index(result[1])], errors)))

p2_scores = list(sorted([reduce(lambda x, y: ((x*5)+y), list(map(lambda token: (Parser.Closings.index(token)+1), incom[1]))) for incom in incoms]))
print("Part 2: %d" % p2_scores[int(len(p2_scores)/2)])
