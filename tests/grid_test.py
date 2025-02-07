import unittest

from classes.grid import detect_grid, Grid
from classes.polygon import Point


class TestDetectGrid(unittest.TestCase):
    def test_empty_input(self):
        self.assertIsNone(detect_grid([]))

    def test_single_point(self):
        self.assertIsNone(detect_grid([Point(0, 0)]))

    def test_line_of_points(self):
        points = [Point(i, 0) for i in range(5)]
        expected = Grid(Point(0, 0), 5, 1, Point(1, 0), Point(0, 0))
        self.assertEqual(detect_grid(points), expected)

    def test_valid_2x2_grid(self):
        points = [
            Point(0, 0), Point(1, 0),
            Point(0, 1), Point(1, 1)
        ]
        expected = Grid(Point(0, 0), 2, 2, Point(1, 0), Point(0, 1))
        self.assertEqual(detect_grid(points), expected)

    def test_valid_3x2_grid(self):
        points = [
            Point(0, 0), Point(1, 0), Point(2, 0),
            Point(0, 1), Point(1, 1), Point(2, 1)
        ]
        expected = Grid(Point(0, 0), 3, 2, Point(1, 0), Point(0, 1))
        self.assertEqual(detect_grid(points), expected)

    def test_missing_point_in_grid(self):
        points = [
            Point(0, 0), Point(1, 0),
            Point(0, 1)
        ]
        self.assertIsNone(detect_grid(points))

    def test_rotated_grid(self):
        points = [
            Point(1, 1), Point(2, 2),
            Point(3, 3), Point(4, 4)
        ]
        expected = Grid(Point(1, 1), 4, 1, Point(1, 1), Point(0, 0))
        self.assertEqual(detect_grid(points), expected)

    def test_large_grid(self):
        points = [Point(x, y) for x in range(5) for y in range(4)]
        expected = Grid(Point(0, 0), 5, 4, Point(1, 0), Point(0, 1))
        self.assertEqual(detect_grid(points), expected)

    def test_irregular_spacing(self):
        points = [
            Point(0, 0), Point(2, 0),
            Point(0, 3), Point(2, 2)
        ]
        self.assertIsNone(detect_grid(points))


if __name__ == "__main__":
    unittest.main()
