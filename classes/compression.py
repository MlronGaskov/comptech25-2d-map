import string
from typing import NamedTuple, Tuple, TextIO, List, Dict

from classes.grid import Grid, detect_grid
from classes.groups import PolygonsGroup, group_polygons
from classes.polygon import Point, Polygon
from classes.prototype import PolygonPrototype


class CompressionEntry(NamedTuple):
    entry_type: string
    prototype: PolygonPrototype
    data: Tuple

    def write_to_file(self, file: TextIO):
        file.write(f"{len(self.prototype.points)} {self.prototype.idx}\n")
        for point in self.prototype.points:
            file.write(f"{point.x} {point.y}\n")
        if self.entry_type == "grid":
            grid: Grid = Grid(*self.data)
            file.write(f"{grid.o.x} {grid.o.y}\n")
            file.write(f"{grid.dim1} {grid.dim2}\n")
            file.write(f"{grid.v1.x} {grid.v1.y}\n")
            file.write(f"{grid.v2.x} {grid.v2.y}\n")
        elif self.entry_type == "shifts":
            file.write(f"{len(self.data)}\n")
            for shift in self.data:
                file.write(f"{shift.x} {shift.y}\n")

    def get_polygons(self) -> List[Polygon]:
        polygons = []
        if self.entry_type == "grid":
            grid: Grid = Grid(*self.data)
            for i in range(grid.dim1):
                for j in range(grid.dim2):
                    polygons.append(Polygon(
                        [Point(
                            point.x + grid.o.x + i * grid.v1.x + j * grid.v2.x,
                            point.y + grid.o.y + i * grid.v1.y + j * grid.v2.y
                        ) for point in self.prototype.points]
                    ))
        else:
            for shift in self.data:
                polygons.append(Polygon(
                    [Point(
                        point.x + shift.x,
                        point.y + shift.y
                    ) for point in self.prototype.points]
                ))
        return polygons


class CompressedMap(NamedTuple):
    compression_entries: Tuple[CompressionEntry, ...]

    def get_polygons(self) -> List[Polygon]:
        return [polygon for entry in self.compression_entries for polygon in entry.get_polygons()]

    def write_to_file(self, file: TextIO):
        file.write(f"{len(self.compression_entries)}\n")
        for entry in self.compression_entries:
            entry.write_to_file(file)


def compress_group(group: PolygonsGroup) -> CompressionEntry:
    points = [p.points[0] for p in group.polygons]
    grid = detect_grid(points)
    if grid:
        return CompressionEntry("grid", group.prototype, tuple(grid))
    else:
        prototype_x, prototype_y = group.prototype.points[0].x, group.prototype.points[0].y
        shifts = tuple([Point(p.points[0].x - prototype_x, p.points[0].y - prototype_y) for p in group.polygons])
        return CompressionEntry("shifts", group.prototype, shifts)


def read_compression_entry_from_file(file: TextIO) -> CompressionEntry:
    points_len, idx = map(int, file.readline().split())
    points = []
    for i in range(points_len):
        x, y = map(int, file.readline().split())
        points.append(Point(x, y))
    prototype = PolygonPrototype(idx, tuple(points))

    line = file.readline()
    if len(line.split()) == 2:
        o = Point(int(line.split()[0]), int(line.split()[1]))
        line = file.readline()
        dim1, dim2 = int(line.split()[0]), int(line.split()[1])
        line = file.readline()
        v1 = Point(int(line.split()[0]), int(line.split()[1]))
        line = file.readline()
        v2 = Point(int(line.split()[0]), int(line.split()[1]))
        data = Grid(o, dim1, dim2, v1, v2)
        entry_type = "grid"
    else:
        shifts = []
        for i in range(int(line)):
            x, y = map(int, file.readline().split())
            shifts.append(Point(x, y))
        data = tuple(shifts)
        entry_type = "shifts"
    return CompressionEntry(entry_type, prototype, data)


def compress_map(polygons: List[Polygon]) -> CompressedMap:
    groups: Dict[int, PolygonsGroup] = group_polygons(polygons)
    compressed_data = []
    for group in groups.values():
        compressed_data.append(compress_group(group))
    return CompressedMap(tuple(compressed_data))


def read_compressed_map_from_file(file_name: string) -> CompressedMap:
    file = open(file_name, "r")
    compressed_data = []
    for i in range(int(file.readline())):
        compressed_data.append(read_compression_entry_from_file(file))
    return CompressedMap(tuple(compressed_data))
