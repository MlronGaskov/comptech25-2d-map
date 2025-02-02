from classes.vector import Vector


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other: "Point"):
        return self.x == other.x and self.y == other.y
