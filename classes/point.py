from classes.vector import Vector


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return Vector(self.x - other.x, self.y - other.y).length() < 0.001
