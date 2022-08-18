import unittest
from pyapp import rotate_clockwise


class RotateClockwise(unittest.TestCase):
    def setUp(self):
        self.rotate_clockwise = rotate_clockwise.rotate_clockwise
    def test_rotate_clockwise(self):
        m3 = [[1,2,3],[4,5,6],[7,8,9]]
        m4 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        m3R = [[7,4,1],[8,5,2],[9,6,3]]
        m4R = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        matrices = [
            (m3, m3R),
            (m4, m4R),
        ]
        for matrix, result in matrices:
            n = len(matrix)
            self.rotate_clockwise(matrix)

            #1. checks if matrix is still a list
            self.assertTrue(isinstance(matrix, list))
            #2. check if 2D matrix size is the same
            self.assertTrue(len(matrix) == len(matrix[0]) == n)
            #3. checks if rotation result is correct
            self.assertTrue(matrix == result)
            