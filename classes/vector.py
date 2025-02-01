from math import sqrt


class Vector:
    """Represents a 2D vector with float components."""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x:.3f}, {self.y:.3f})"

    def length(self) -> float:
        """Returns the length (magnitude) of the vector."""
        return sqrt(self.x ** 2 + self.y ** 2)

    def scale(self, factor: float):
        """Scales the vector by a given factor."""
        return Vector(self.x * factor, self.y * factor)

    def __eq__(self, other: "Vector") -> bool:
        """Checks if two vectors are equivalent with a small margin of error."""
        d = Vector(self.x - other.x, self.y - other.y)
        return d.length() < 0.001
