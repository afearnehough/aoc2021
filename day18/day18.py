import ast, math

# input = [ast.literal_eval(line) for line in open("input.txt").read().splitlines()]

class SFN:
    class Element:
        def __init__(self, value, depth):
            self.v = value
            self.d = depth

    def __init__(self, input):
        self.elems = []
        self._traverse_tree(input)

    def _traverse_tree(self, node, depth=-1):
        if isinstance(node, list):
            for child_node in node:
                self._traverse_tree(child_node, (depth+1))
        else:
            self.elems.append(SFN.Element(node, depth))

    def add(self, sfn):
        self.elems += sfn.elems
        for el in self.elems:
            el.d += 1

    def reduce(self):
        pass

    def explode(self):
        i = 0
        while i < (len(self.elems)-1):
            a, b = self.elems[i], self.elems[i+1]
            if a.d == b.d and a.d >= 4:
                self.add_value((i-1), self.elems[i].v)
                self.add_value((i+2), self.elems[i+1].v)

                if len(self.elems):

                self.elems[i] = SFN.Element(0, (a.d-1))
                self.elems.pop(i+1)
            i += 1

    def split(self);
        pass

    def get_elems(self):
        return [el.v for el in self.elems]

sfn = SFN([[[[4,3],4],4],[7,[[8,4],9]]])
print(sfn.get_elems())
sfn.add(SFN([1,1]))
print(sfn.get_elems())
sfn.reduce()
print(sfn.get_elems())