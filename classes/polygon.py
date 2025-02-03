from typing import List, NamedTuple


class Point(NamedTuple):
    x: int
    y: int


class Polygon:
    def __init__(self, points: List[Point]):
        if len(points) < 3:
            raise ValueError("Polygon must contain at least 3 points.")

        self.points = Polygon.reorder_points(points)

    def __repr__(self):
        return f"Polygon({self.points})"

    @classmethod
    def find_rightmost_upper_point_idx(cls, points: List[Point]) -> int:
        return max(range(len(points)), key=lambda idx: (points[idx].x, points[idx].y))

    @classmethod
    def cross_product(cls, a: Point, b: Point, c: Point) -> int:
        return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)

    @classmethod
    def reorder_points(cls, points: List[Point]) -> List[Point]:
        start_index = Polygon.find_rightmost_upper_point_idx(points)
        a = points[start_index]
        b = points[(start_index + 1) % len(points)]
        c = points[(start_index - 1) % len(points)]

        normalized_points = points[start_index:] + points[:start_index]

        if Polygon.cross_product(a, b, c) < 0:
            normalized_points.reverse()
            normalized_points = [normalized_points[-1]] + normalized_points[:-1]

        return normalized_points


def load(filename: str) -> List[Polygon]:
    polygons = []

    with open(filename, "r") as file:
        lines = file.readlines()
        index = 1

        num_polygons = int(lines[0].strip())
        for _ in range(num_polygons):
            num_points = int(lines[index].strip())
            index += 1

            points = []
            for _ in range(num_points):
                x, y = map(int, lines[index].strip().split())
                points.append(Point(x, y))
                index += 1

            polygons.append(Polygon(points))

    return polygons