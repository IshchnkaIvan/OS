from unittest import TestCase
import time
import numpy

from main import parallel_matrix_multiplication


class Test(TestCase):
    def test_parallel_matrix_multiplication_results(self):
        first_matrix = numpy.random.randint(low=0, high=10, size=(500, 500), dtype=int)
        second_matrix = numpy.random.randint(low=0, high=10, size=(500, 100), dtype=int)
        start_time = time.time()
        result_matrix = parallel_matrix_multiplication(4, first_matrix, second_matrix)
        print(result_matrix)
        print('parallel_matrix_multiplication result:  {} second'.format(time.time() - start_time))
        self.assertEqual(result_matrix.tolist(),
                         first_matrix.dot(second_matrix).tolist())


    def test_parallel_matrix_multiplication_types(self):
        self.assertRaises(TypeError, parallel_matrix_multiplication, 1.1, numpy.array([[1, 2]]),
                          numpy.array([[1], [2]]))

    def test_parallel_matrix_multiplication_values(self):
        self.assertRaises(ValueError, parallel_matrix_multiplication, 0, numpy.array([[5, 1]]), numpy.array([[5]]))
