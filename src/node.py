from functools import total_ordering


@total_ordering
class Node:
    keyCount = 1

    def __repr__(self):
        return repr('node:' + str(self.key))

    def __lt__(self, other):
        return self.tag < other.tag

    def __eq__(self, other):
        return self.key == other.key and self.tag == other.tag and self.info == other.info

    def __init__(self, key=-2, tag=-1, info="", lastNei=-1, neiCount=0, pos=""):
        if key == -2:
            self.key = Node.keyCount
            Node.keyCount += 1
        else:
            self.key = key
        self.tag = tag
        self.info = info
        self.lastNei = lastNei
        self.neiCount = neiCount
        self.pos=pos

    def __copy__(self):
        n1 = Node()
        n1.key = self.key
        n1.tag = self.tag
        n1.info = self.info
        n1.lastNei = self.lastNei
        n1.neiCount = self.neiCount
