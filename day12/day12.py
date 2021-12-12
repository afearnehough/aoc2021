class Cave:
    def __init__(self, designation):
        self.designation = designation
        self.is_small = True if designation == designation.lower() else False
        self.connections = []

class CaveGraph:
    def __init__(self, connections):
        self.caves = {}

        for connection in connections:
            (des_a, des_b) = connection.split("-")
            self.connect(des_a, des_b)
            self.connect(des_b, des_a)

    def connect(self, a, b):
        if a not in self.caves:
            self.caves[a] = Cave(a)
        self.caves[a].connections.append(b)

    def find_paths(self, visit_limit=2):
        paths = []
        stack = [(self.caves["start"], 0, visit_limit)]
        build_path = lambda: list(map(lambda entry: entry[0].designation, stack))

        while len(stack):
            (cave, direction, visit_limit) = stack.pop()
            if cave.designation == "end":
                paths.append(build_path()+[cave.designation])
            else:
                visit_count = build_path().count(cave.designation)
                if not cave.is_small or visit_count < visit_limit:
                    if direction < len(cave.connections):
                        stack.append((cave, (direction+1), visit_limit))
                        if cave.connections[direction] != "start":
                            if cave.is_small and visit_count == 1:
                                visit_limit -= 1
                            stack.append((self.caves[cave.connections[direction]], 0, visit_limit))
        return paths


graph = CaveGraph(open("input.txt").read().splitlines())
print("Part 1: %d paths" % len(graph.find_paths(1)))
print("Part 2: %d paths" % len(graph.find_paths(2)))