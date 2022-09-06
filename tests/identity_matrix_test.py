from ctypes import resize
import unittest
from pyapp import identity_matrix

class IdentityMatrix(unittest.TestCase):

    def setUp(self) -> None:
        self.identity_matrix = identity_matrix.identity_matrix

    def test_identity(self):
        m3 = [[1,2,3],[4,5,6],[7,8,9]]
        m4 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        m3R = [[1,0,0],[0,1,0],[0,0,1]]
        m4R = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
        matrices = [
            (m3, m3R),
            (m4, m4R),
        ]

        for matrix, result in matrices:
            n = len(matrix)
            result = self.identity_matrix(matrix)

            #1. checks if matrix is still a list
            self.assertTrue(isinstance(result, list))
            #2. check if 2D matrix size is the same
            self.assertTrue(len(result) == len(result[0]) == n)
            #3. checks if rotation result is correct
            self.assertTrue(result == result)

    
