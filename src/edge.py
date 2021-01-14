from functools import total_ordering


class Edge:
    def __repr__(self):
        return repr('edge:' + str(self.src)+','+str(self.dest))
    def __eq__(self, other):
        return self.src == other.src and self.dest == other.dest and self.weight == other.weight
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight
