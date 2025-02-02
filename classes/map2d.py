from typing import List
from classes.point import Point
from classes.polygon import Polygon


class Map2D:
    def __init__(self):
        self.polygons: List[Polygon] = []

    def load_from_file(self, filename: str):
        self.polygons = []

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

                self.polygons.append(Polygon(points))

    def __repr__(self):
        return f"Map2D({self.polygons})"

