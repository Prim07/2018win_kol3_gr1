import unittest
import MatrixLibrary

class MatrixLibraryTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_none_is_returning_when_different_size_matrices_are_added(self):
        matrix1 = MatrixLibrary.Matrix(2, 2, 2, 2)
        matrix2 = MatrixLibrary.Matrix(2, 2, 2, 2, 2, 2, 2, 2, 2)
        self.assertEqual(matrix1.add(matrix2), None)

    def test_matrix_add_method(self):
        matrix1 = MatrixLibrary.Matrix(2, 2, 2, 2)
        matrix2 = MatrixLibrary.Matrix(2, 2, 2, 2)
        added_matrices = MatrixLibrary.Matrix(4, 4, 4, 4)
        self.assertEqual(matrix1.add(matrix2).matrix, added_matrices.matrix)