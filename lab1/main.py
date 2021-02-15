import numpy
import sys
import argparse
import time
import multiprocessing
from functools import reduce


def calculate_matrix(info):
    start_index, size, first_matrix, second_matrix = info
    part_of_result_matrix = numpy.zeros((first_matrix.shape[0], second_matrix.shape[0]), dtype=int)
    print("Thread lol")
    for i in range(size):
        shape = part_of_result_matrix.shape
        summa = 0
        row = (start_index + i) // shape[1]
        col = (start_index + i) % shape[1]
        for j in range(len(first_matrix[row])):
            summa += first_matrix[row][j] * second_matrix[col][j]
        part_of_result_matrix[row][col] = summa
    print(part_of_result_matrix.flatten()[start_index:start_index + size])
    return part_of_result_matrix.flatten()[start_index:start_index + size]


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--threads', nargs='?', default=1)
    parser.add_argument('-s', '--sizes', nargs='+', default=[0, 0, 0])
    return parser


def separate_data(count, n, l):
    size = n * l // count
    indexs = []
    sizes = []
    ost = n * l - size * count
    index = 0
    for i in range(count):
        if ost > 0:
            sizes.append(size + 1)
            ost -= 1
        else:
            sizes.append(size)
        indexs.append(index)
        index += sizes[i]
    return indexs, sizes


def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    # n&m - sizes of matrix A, m & l -sizes of matrix B

    n = int(namespace.sizes[0])
    m = int(namespace.sizes[1])
    l = int(namespace.sizes[2])
    count_threads = int(namespace.threads)
    first_matrix = numpy.random.randint(low=0, high=10, size=(n, m), dtype=int)
    second_matrix = numpy.random.randint(low=0, high=10, size=(m, l), dtype=int)
    # result_matrix = numpy.zeros(shape=(n, l), dtype=int)
    print(first_matrix)
    print()
    print(second_matrix)
    #проверка
    #print(first_matrix.dot(second_matrix))
    transpose_second_matrix = numpy.transpose(second_matrix)
    print()
    print(transpose_second_matrix)
    print()
    # print(result_matrix)
    threads = []
    indexs, sizes = separate_data(count_threads, n, l)
    # first_rows = []
    # second_rows = []
    # for i in range(count_threads):
    #     first_rows.append([])
    #     second_rows.append([])
    #     for j in range(indexs[i] // n, (indexs[i] + sizes[i]) // n):
    #         first_rows[i].append(first_matrix[j])
    #     for k in range(indexs[i] % l, (indexs[i] + sizes[i]) % l):
    #         second_rows[i].append(second_matrix[k])
    info = []
    for i in range(count_threads):
        info.append([indexs[i], sizes[i], first_matrix, transpose_second_matrix])
    start_time = time.time()
    # for i in range(count_threads):
    #     thread = multiprocessing.Process(target=calculate_matrix,
    #                               args=(indexs[i], sizes[i], first_matrix, transpose_second_matrix, result_matrix))
    #     threads.append(thread)
    #     thread.start()
    # for thread in threads:
    #     thread.join()
    pool = multiprocessing.Pool(processes=count_threads)
    auf = reduce(lambda a, b: numpy.concatenate([a, b]), pool.map(calculate_matrix, info))
    # print('result:')
    # print(result_matrix)
    print('auf:')
    print(auf.reshape((n, l)))

    print('seconds: ' + str(time.time() - start_time))


if __name__ == "__main__":
    main()
