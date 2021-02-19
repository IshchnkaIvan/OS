import multiprocessing
from functools import reduce
import numpy


def calculate_matrix(info: tuple) -> numpy.array:
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


def separate_data(count: int, row_count: int, column_count: int) -> tuple[int]:
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


def parallel_matrix_multiplication(processes_count: int, first_matrix: numpy.array,
                                   second_matrix: numpy.array) -> numpy.array:
    if type(processes_count) != int:
        raise TypeError("'processes_count' must be int, not {}".format(type(processes_count)))
    if processes_count < 1:
        raise ValueError("'processes_count' must be positive number")
    transpose_second_matrix = numpy.transpose(second_matrix)
    n = first_matrix.shape[0]
    L = second_matrix.shape[1]
    indexes, sizes = separate_data(count=processes_count, row_count=n, column_count=L)
    info = [[indexes[i], sizes[i], first_matrix, transpose_second_matrix] for i in range(processes_count)]
    pool = multiprocessing.Pool(processes=processes_count)
    result_matrix = reduce(lambda a, b: numpy.concatenate([a, b]), pool.map(calculate_matrix, info)).reshape((n, L))
    pool.close()
    return result_matrix
