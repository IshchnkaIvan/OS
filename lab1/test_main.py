from unittest import TestCase

import numpy

from main import parallel_matrix_multiplication


class Test(TestCase):
    def test_parallel_matrix_multiplication_results(self):
        first_matrix = numpy.random.randint(low=0, high=10, size=(5, 6), dtype=int)
        second_matrix = numpy.random.randint(low=0, high=10, size=(6, 7), dtype=int)
        self.assertEqual(parallel_matrix_multiplication(4, first_matrix, second_matrix).tolist(),
                         first_matrix.dot(second_matrix).tolist())
        self.assertEqual(parallel_matrix_multiplication(1, first_matrix, second_matrix).tolist(),
                         first_matrix.dot(second_matrix).tolist())

    def test_parallel_matrix_multiplication_types(self):
        self.assertRaises(TypeError, parallel_matrix_multiplication, 1.1, [[1, 2]], [[1], [2]])

    def test_parallel_matrix_multiplication_values(self):
        self.assertRaises(ValueError, parallel_matrix_multiplication, 0, [[5, 1]], [[5]])
