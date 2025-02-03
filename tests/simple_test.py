import unittest
from typing import List

from classes.groups import group_polygons
from classes.polygon import Polygon, load


class TestPolygon(unittest.TestCase):

    def test_polygon_grouping(self):
        filename: str = "../map-examples/test6.txt"
        polygons: List[Polygon] = load(filename)
        groups = group_polygons(polygons)
        print(groups)