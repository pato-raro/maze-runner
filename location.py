import math

class Location:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.g_score = 1
        self.f_score = 1
        self.parent = None

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Location):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))

    @staticmethod
    def sort(locations):
        return sorted(locations, key=lambda loc: (loc.x, loc.y))

    @staticmethod
    def heuristic(a: 'Location', b: 'Location') -> float:
        return math.dist((a.x, a.y), (b.x, b.y))
