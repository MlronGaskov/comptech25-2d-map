from typing import List
from classes.point import Point
from classes.polygon import Polygon


class Map2D:
    def __init__(self):
        self.polygons: List[Polygon] = []

    def load_from_file(self, filename: str):
        self.polygons = []

        with open(filename, "r") as file:
            for line in file:
                points = []
                point_strings = line.strip().split(";")
                for point_str in point_strings:
                    x, y = map(float, point_str.split(","))
                    points.append(Point(x, y))
                self.polygons.append(Polygon(points))

    def __repr__(self):
        return f"Map2D({self.polygons})"
