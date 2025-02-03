from typing import List, Dict
import matplotlib.pyplot as plt
import random
from shapely.geometry import Polygon as ShapelyPolygon

from classes.groups import group_polygons
from classes.polygon import Polygon, load


class Visualizer:
    @staticmethod
    def draw_polygons(filename: str):
        polygons: List[Polygon] = load(filename)

        fig, ax = plt.subplots()

        for polygon in polygons:
            shapely_poly = ShapelyPolygon([(p.x, p.y) for p in polygon.points])
            x, y = shapely_poly.exterior.xy
            ax.plot(x, y, marker="o", linestyle="-", label="Polygon")

        ax.set_aspect("equal")
        plt.grid(True)
        plt.show()

    @staticmethod
    def draw_groups(filename: str):
        polygons: List[Polygon] = load(filename)
        groups = group_polygons(polygons)

        fig, ax = plt.subplots()
        colors = [
            (random.random(), random.random(), random.random()) for _ in range(len(groups))
        ]

        for group_idx, group in enumerate(groups):
            color = colors[group_idx]

            for polygon in groups[group].polygons:
                shapely_poly = ShapelyPolygon([(p.x, p.y) for p in polygon.points])
                x, y = shapely_poly.exterior.xy
                ax.fill(x, y, color=color, alpha=0.5, edgecolor="black", linewidth=1)

        ax.set_aspect("equal")
        plt.grid(True)
        plt.show()


if __name__ == '__main__':
    Visualizer.draw_groups("./map-examples/test5.txt")