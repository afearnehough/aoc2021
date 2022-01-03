import ast, math

class SFN:
    class Element:
        def __init__(self, value, depth):
            self.v = value
            self.d = depth

    def __init__(self, tree=[]):
        self.elems = []
        self._traverse_tree(tree)

    def _traverse_tree(self, node, depth=-1):
        if isinstance(node, list):
            for child in node:
                self._traverse_tree(child, (depth+1))
        else:
            self.elems.append(SFN.Element(node, depth))

    def add(self, sfn):
        self.elems += sfn.elems
        for el in self.elems:
            el.d += 1
        self.reduce()

    def reduce(self):
        self.explode()
        while self.split():
            self.explode()

    def split(self):
        i = 0
        while i < len(self.elems):
            if self.elems[i].v >= 10:
                val = self.elems[i].v
                self.elems[i].v = math.floor(val/2)
                self.elems[i].d += 1
                self.elems.insert((i+1), SFN.Element(math.ceil(val/2), self.elems[i].d))
                return True
            i += 1
        return False

    def explode(self):
        i = 0
        while i < (len(self.elems)-1):
            a, b = self.elems[i], self.elems[i+1]
            if a.d == b.d and a.d >= 4:
                if (i-1) >= 0: self.elems[i-1].v += self.elems[i].v
                if (i+2) < len(self.elems): self.elems[i+2].v += self.elems[i+1].v
                self.elems[i] = SFN.Element(0, (a.d-1))
                self.elems.pop(i+1)
            i += 1

    def magnitude(self):
        pass


    def get_elems(self):
        return [el.v for el in self.elems]

input = [ast.literal_eval(line) for line in open("input.txt").read().splitlines()]
total = SFN(input[0])
for number in input[1:]:
    total.add(SFN(number))
print("Part 1 final sum: %s" % total.get_elems())
print("Part 1 magnitude: %d" % total.magnitude())
