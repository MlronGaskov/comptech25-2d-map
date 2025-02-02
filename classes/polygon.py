from typing import List
from classes.point import Point
from classes.vector import Vector


def _find_start_point(points: List[Point]) -> int:
    """Finds the index of the rightmost highest point."""
    return max(range(len(points)), key=lambda idx: (points[idx].x, points[idx].y))


def _cross_product(A: Point, B: Point, C: Point) -> float:
    """
    Computes the cross product to determine orientation.
    If result > 0 → counterclockwise (CCW).
    If result < 0 → clockwise (CW).
    """
    return (B.x - A.x) * (C.y - A.y) - (B.y - A.y) * (C.x - A.x)


def _normalize_points(points: List[Point]) -> List[Point]:
    """Rearranges points so that they start from the rightmost highest point and go counterclockwise."""
    start_index = _find_start_point(points)
    A = points[start_index]
    B = points[(start_index + 1) % len(points)]
    C = points[(start_index - 1) % len(points)]

    # Arrange points to start from the highest-rightmost point
    normalized_points = points[start_index:] + points[:start_index]

    # Ensure counterclockwise order
    if _cross_product(A, B, C) < 0:
        normalized_points.reverse()
        # Ensure the start point remains first after reversal
        normalized_points = [normalized_points[-1]] + normalized_points[:-1]

    return normalized_points


class Polygon:
    def __init__(self, points: List[Point]):
        if len(points) < 3:
            raise ValueError("Polygon must contain at least 3 points.")

        self.points = _normalize_points(points)

    def get_type(self) -> List[Vector]:
        """Returns a list of normalized vectors representing the polygon's edges."""
        vectors = []

        # Create vectors for each edge
        for i in range(len(self.points)):
            A = self.points[i]
            B = self.points[(i + 1) % len(self.points)]
            vector = Vector(B.x - A.x, B.y - A.y)
            vectors.append(vector)

        #first_length = vectors[0].length()
        #scale_factor = 1 / first_length

        #for i in range(0, len(vectors)):
        #    vectors[i] = vectors[i].scale(scale_factor)

        return vectors

    def __eq__(self, other: "Polygon") -> bool:
        """Checks if two polygons are equivalent."""
        if not isinstance(other, Polygon) or len(self.points) != len(other.points):
            return False

        v1 = self.get_type()
        v2 = other.get_type()

        if len(v1) != len(v2):
            return False

        if all(v1[i] == (v2[i % len(v2)]) for i in range(len(v1))):
            return True

        return False

    def __repr__(self):
        return f"Polygon({self.points})"
