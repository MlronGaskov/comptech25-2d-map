from math import sqrt


class Vector:
    """Represents a 2D vector with float components."""

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x:.3f}, {self.y:.3f})"

    def length(self) -> float:
        """Returns the length (magnitude) of the vector."""
        return sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other: "Vector") -> bool:
        """Checks if two vectors are equivalent."""
        return other.x == self.x and other.y == self.y
