from typing import List, Dict

from classes.polygon import Polygon
from classes.prototype import PolygonPrototype, PolygonPrototypesPool


class PolygonsGroup:
    def __init__(self, prototype: PolygonPrototype):
        self.prototype = prototype
        self.polygons = []

    def __repr__(self):
        return f"PolygonsGroup({len(self.polygons)} polygons x {len(self.prototype.points)} points)"


def group_polygons(polygons: List[Polygon]) -> Dict[int, PolygonsGroup]:
    pool: PolygonPrototypesPool = PolygonPrototypesPool()
    result: Dict[int, PolygonsGroup] = {}
    for polygon in polygons:
        prototype = pool.get_prototype(polygon)
        if not prototype.idx in result:
            result[prototype.idx] = PolygonsGroup(prototype)
        result[prototype.idx].polygons.append(polygon)
    return result