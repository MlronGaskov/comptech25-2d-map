from typing import NamedTuple, Set, Optional, List

from classes.polygon import Point


class Grid(NamedTuple):
    o: Point
    dim1: int
    dim2: int
    v1: Point
    v2: Point


def find_vector(points: Set[Point], bound_clockwise: bool) -> Point:
    def cp(a: Point, b: Point) -> int:
        return a.x * b.y - a.y * b.x

    def ln(a: Point) -> int:
        return a.x ** 2 + a.y ** 2

    v: Optional[Point] = None
    for p in points:
        if p == Point(0, 0):
            continue
        if v is None:
             v = p
        elif cp(v, p) == 0:
            if ln(v) > ln(p):
                v = p
        elif (cp(v, p) > 0) != bound_clockwise:
            v = p
    if v is None:
        raise ValueError('Cannot find vector')
    return v


def find_dim(points: Set[Point], v: Point) -> int:
    if v == Point(0, 0):
        return 1
    dim = 1
    while Point(dim * v.x, dim * v.y) in points:
        dim += 1
    return dim


def detect_grid(points: List[Point]) -> Optional[Grid]:
    if not points:
        return None

    o = min(points, key=lambda p: (p.y, p.x))

    points_set = {Point(x - o.x, y - o.y) for x, y in points}
    if len(points_set) == 1:
        return None
    v1 = find_vector(points_set, True)
    v2 = find_vector(points_set, False)
    if v1 == v2:
        v2 = Point(0, 0)
    dim1 = find_dim(points_set, v1)
    dim2 = find_dim(points_set, v2)
    if dim1 * dim2 != len(points):
        return None
    for i in range(dim1):
        for j in range(dim2):
            if Point(i * v1.x + j * v2.x, i * v1.y + j * v2.y) not in points_set:
                return None
    return Grid(o, dim1, dim2, v1, v2)