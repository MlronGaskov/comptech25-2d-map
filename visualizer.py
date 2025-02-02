import matplotlib.pyplot as plt
from shapely.geometry import Polygon as ShapelyPolygon
from classes.map2d import Map2D


class MapVisualizer:
    @staticmethod
    def draw(map_2d: Map2D):
        fig, ax = plt.subplots()

        for polygon in map_2d.polygons:
            shapely_poly = ShapelyPolygon([(p.x, p.y) for p in polygon.points])

            x, y = shapely_poly.exterior.xy
            ax.plot(x, y, marker="o", linestyle="-", label="Polygon")

        ax.set_aspect("equal")
        plt.grid(True)
        plt.show()


map_2d = Map2D()
map_2d.load_from_file("./map-examples/test5.txt")

MapVisualizer.draw(map_2d)
