from typing import List, Dict
import matplotlib.pyplot as plt
import random
from shapely.geometry import Polygon as ShapelyPolygon
from matplotlib.widgets import Button

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
        plt.title("Grouped Polygons Visualization")

        ax_zoom_in = plt.axes([0.7, 0.05, 0.1, 0.075])
        ax_zoom_out = plt.axes([0.81, 0.05, 0.1, 0.075])
        btn_zoom_in = Button(ax_zoom_in, "Zoom In")
        btn_zoom_out = Button(ax_zoom_out, "Zoom Out")

        def zoom_in(event):
            ax.set_xlim(ax.get_xlim()[0] * 0.9, ax.get_xlim()[1] * 0.9)
            ax.set_ylim(ax.get_ylim()[0] * 0.9, ax.get_ylim()[1] * 0.9)
            plt.draw()

        def zoom_out(event):
            ax.set_xlim(ax.get_xlim()[0] * 1.1, ax.get_xlim()[1] * 1.1)
            ax.set_ylim(ax.get_ylim()[0] * 1.1, ax.get_ylim()[1] * 1.1)
            plt.draw()

        btn_zoom_in.on_clicked(zoom_in)
        btn_zoom_out.on_clicked(zoom_out)

        plt.show()


if __name__ == '__main__':
    Visualizer.draw_groups("./map-examples/test11.txt")
