import unittest

from classes.map2d import Map2D
from classes.point import Point
from classes.polygon import Polygon


class TestPolygon(unittest.TestCase):

    def rotate_list(self, lst, shift):
        """Вспомогательная функция для циклического сдвига списка."""
        return lst[shift:] + lst[:shift]

    def test_polygon_normalization(self):
        """Проверяем, что точки нормализуются корректно (старт с правой верхней точки)."""
        raw_points = [
            [Point(0, 0), Point(4, 0), Point(4, 4), Point(0, 4)],  # Квадрат
            [Point(2, 1), Point(5, 3), Point(4, 6), Point(1, 4)],  # Разный порядок
            [Point(3, 2), Point(6, 5), Point(4, 7), Point(2, 5)],  # Другая форма
        ]

        expected_normalized = [
            [Point(4, 4), Point(0, 4), Point(0, 0), Point(4, 0)],  # Ожидаемый порядок (CCW)
            [Point(5, 3), Point(4, 6), Point(1, 4), Point(2, 1)],
            [Point(6, 5), Point(4, 7), Point(2, 5), Point(3, 2)],
        ]

        for i in range(len(raw_points)):
            poly = Polygon(raw_points[i])
            self.assertEqual(poly.points, expected_normalized[i])

    def test_polygon_equivalence_rotations(self):
        """Проверяем, что полигоны эквивалентны при поворотах и циклических сдвигах."""
        base_points = [Point(0, 0), Point(4, 0), Point(4, 4), Point(0, 4)]
        base_polygon = Polygon(base_points)

        for shift in range(len(base_points)):
            rotated = self.rotate_list(base_points, shift)
            rotated_polygon = Polygon(rotated)
            self.assertEqual(base_polygon, rotated_polygon)

    def test_polygon_equivalence_reversals(self):
        """Проверяем, что полигоны эквивалентны при реверсе порядка точек."""
        base_points = [Point(0, 0), Point(4, 0), Point(4, 4), Point(0, 4)]
        base_polygon = Polygon(base_points)

        reversed_polygon = Polygon(list(reversed(base_points)))
        self.assertEqual(base_polygon, reversed_polygon)

    def test_polygon_equivalence_rotations_reversals(self):
        """Проверяем полигоны при любых сдвигах + реверсе."""
        base_points = [Point(1, 1), Point(4, 1), Point(5, 3), Point(3, 5), Point(0, 4)]
        base_polygon = Polygon(base_points)

        for shift in range(len(base_points)):
            rotated = self.rotate_list(base_points, shift)
            rotated_polygon = Polygon(rotated)
            self.assertEqual(base_polygon, rotated_polygon)

            reversed_rotated_polygon = Polygon(list(reversed(rotated)))
            self.assertEqual(base_polygon, reversed_rotated_polygon)

    def test_polygon_non_equivalence(self):
        """Проверяем, что разные полигоны не считаются эквивалентными."""
        poly1 = Polygon([Point(0, 0), Point(4, 0), Point(4, 4), Point(0, 4)])
        poly2 = Polygon([Point(1, 1), Point(3, 1), Point(3, 3)])  # Треугольник

        self.assertNotEqual(poly1, poly2)

    def test_polygon_equivalence_0(self):
        map_2d = Map2D()
        map_2d.load_from_file("../map-examples/test0.txt")
        for i in range(len(map_2d.polygons)):
            for j in range(i, len(map_2d.polygons)):
                self.assertEqual(map_2d.polygons[i], map_2d.polygons[j])

    def test_polygon_equivalence_1(self):
        map_2d = Map2D()
        map_2d.load_from_file("../map-examples/test1.txt")
        for i in range(len(map_2d.polygons)):
            for j in range(i, len(map_2d.polygons)):
                self.assertEqual(map_2d.polygons[i], map_2d.polygons[j])

    def test_polygon_equivalence_2(self):
        map_2d = Map2D()
        map_2d.load_from_file("../map-examples/test2.txt")
        for i in range(len(map_2d.polygons)):
            for j in range(i, len(map_2d.polygons)):
                self.assertEqual(map_2d.polygons[i], map_2d.polygons[j])

    def test_polygon_equivalence_3(self):
        map_2d = Map2D()
        map_2d.load_from_file("../map-examples/test3.txt")
        for i in range(len(map_2d.polygons)):
            for j in range(i, len(map_2d.polygons)):
                self.assertEqual(map_2d.polygons[i], map_2d.polygons[j])

    def test_polygon_equivalence_4(self):
        map_2d = Map2D()
        map_2d.load_from_file("../map-examples/test4.txt")
        for i in range(len(map_2d.polygons)):
            for j in range(i, len(map_2d.polygons)):
                self.assertEqual(map_2d.polygons[i], map_2d.polygons[j])

    def test_polygon_equivalence_5(self):
        map_2d = Map2D()
        map_2d.load_from_file("../map-examples/test5.txt")
        for i in range(len(map_2d.polygons)):
            for j in range(i, len(map_2d.polygons)):
                self.assertEqual(map_2d.polygons[i], map_2d.polygons[j])


if __name__ == "__main__":
    unittest.main()
