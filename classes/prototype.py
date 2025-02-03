from typing import Tuple, Dict
from classes.polygon import Point, Polygon


class PolygonPrototype:
    def __init__(self, idx: int, points: Tuple[Point, ...]):
        self.idx = idx
        self.points = points

    def __repr__(self):
        return f"PolygonPrototype({self.points})"


class PolygonPrototypesPool:
    def __init__(self):
        self.prototypes_dict: Dict[Tuple, PolygonPrototype] = {}
        self.prototypes_list = []

    def get_prototype(self, polygon: Polygon) -> PolygonPrototype:
        prototype_key = PolygonPrototypesPool.get_relative_points(polygon)

        if prototype_key not in self.prototypes_dict:
            prototype = PolygonPrototype(len(self.prototypes_dict), prototype_key)
            self.prototypes_dict[prototype_key] = prototype
            self.prototypes_list.append(prototype)
            return prototype
        else:
            return self.prototypes_dict[prototype_key]

    @classmethod
    def get_relative_points(cls, polygon: Polygon) -> Tuple[Point, ...]:
        if not polygon.points:
            return ()

        first_x, first_y = polygon.points[0].x, polygon.points[0].y
        return tuple(Point(p.x - first_x, p.y - first_y) for p in polygon.points)

    def __repr__(self):
        return f"PolygonPrototypesPool({len(self.prototypes_dict)} prototypes stored)"
