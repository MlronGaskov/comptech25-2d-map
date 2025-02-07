import string
from typing import List, Dict, Set

from classes.compression import read_compressed_map_from_file
from classes.polygon import load, Polygon, Point
from classes.prototype import PolygonPrototypesPool, PolygonPrototype


def compare_polygons(expected: List[Polygon], polygons: List[Polygon]):
    if len(expected) != len(polygons):
        return False
    pool: PolygonPrototypesPool = PolygonPrototypesPool()
    polygons_dict: Dict[Point, Set[PolygonPrototype]] = {}
    for polygon in expected:
        prototype = pool.get_prototype(polygon)
        if polygon.points[0] not in polygons_dict:
            polygons_dict[polygon.points[0]] = set()
        polygons_dict[polygon.points[0]].add(prototype)

    for polygon in polygons:
        prototype = pool.get_prototype(polygon)
        if polygon.points[0] not in polygons_dict:
            return False
        if prototype not in polygons_dict[polygon.points[0]]:
            return False
        polygons_dict[polygon.points[0]].remove(prototype)
    return True


def is_compression_valid(expected_file: string, compressed_file: string) -> bool:
    expected_polygons = load(expected_file)
    polygons_from_compressed_file = read_compressed_map_from_file(compressed_file).get_polygons()
    return compare_polygons(expected_polygons, polygons_from_compressed_file)


if __name__ == '__main__':
    for i in range(13):
        print(i, is_compression_valid(f"./map-examples/test{i}.txt", f"./compressed/test{i}.txt"))
