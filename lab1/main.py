import numpy
import sys
import argparse
import time
import multiprocessing
from functools import reduce


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--threads', nargs='?', default=1)
    parser.add_argument('-s', '--sizes', nargs='+', default=[0, 0, 0])
    return parser


def calculate_matrix(info):
    start_index, size, first_matrix, second_matrix = info
    part_of_result_matrix = numpy.zeros((first_matrix.shape[0], second_matrix.shape[0]), dtype=int)
    for i in range(size):
        shape = part_of_result_matrix.shape
        summa = 0
        row = (start_index + i) // shape[1]
        col = (start_index + i) % shape[1]
        for j in range(len(first_matrix[row])):
            summa += first_matrix[row][j] * second_matrix[col][j]
        part_of_result_matrix[row][col] = summa
    return part_of_result_matrix.flatten()[start_index:start_index + size]


def separate_data(count, row_count, column_count):
    size = row_count * column_count // count
    indexes = []
    sizes = []
    ost = row_count * column_count - size * count
    index = 0
    for i in range(count):
        if ost > 0:
            sizes.append(size + 1)
            ost -= 1
        else:
            sizes.append(size)
        indexes.append(index)
        index += sizes[i]
    return indexes, sizes


def parallel_matrix_multiplication(processes_count, first_matrix, second_matrix):
    transpose_second_matrix = numpy.transpose(second_matrix)
    indexes, sizes = separate_data(count=processes_count, row_count=n, column_count=L)
    info = [[indexes[i], sizes[i], first_matrix, transpose_second_matrix] for i in range(processes_count)]
    pool = multiprocessing.Pool(processes=processes_count)
    return reduce(lambda a, b: numpy.concatenate([a, b]), pool.map(calculate_matrix, info)).reshape((n, L))


if __name__ == "__main__":
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    # n&m - sizes of matrix A, m & L -sizes of matrix B
    n = int(namespace.sizes[0])
    m = int(namespace.sizes[1])
    L = int(namespace.sizes[2])
    processes_count = int(namespace.threads)
    first_matrix = numpy.random.randint(low=0, high=10, size=(n, m), dtype=int)
    second_matrix = numpy.random.randint(low=0, high=10, size=(m, L), dtype=int)
    start_time = time.time()
    result_matrix = parallel_matrix_multiplication(processes_count, first_matrix, second_matrix)
    print(result_matrix)
    print('parallel_matrix_multiplication result:  {} second'.format(time.time() - start_time))
