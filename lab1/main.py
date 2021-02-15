import numpy
import random
import sys
import argparse
import time
import multiprocessing


def transpose_matrix(matrix):
    new_matrix = numpy.empty((matrix.shape[1], matrix.shape[0]), dtype=int)
    for i in range(0, matrix.shape[1]):
        for j in range(0, matrix.shape[0]):
            new_matrix[i][j] = matrix[j][i]
    return new_matrix


def calculate_matrix(start_index, size, first_matrix, second_matrix, result_matrix):
    print("Thread lol")
    for i in range(size):
        shape = result_matrix.shape
        summa = 0
        row = (start_index + i) // shape[1]
        col = (start_index + i) % shape[1]
        for j in range(len(first_matrix[row])):
            summa += first_matrix[row][j] * second_matrix[col][j]
        result_matrix[row][col] = summa


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--threads', nargs='?', default=1)
    parser.add_argument('-s', '--sizes', nargs='+', default=[0, 0, 0])
    return parser


def create_matrix(n, m, is_empty):
    arr = numpy.empty((n, m), dtype=int)
    if not is_empty:
        for i in range(0, n):
            for j in range(0, m):
                arr[i][j] = random.randint(0, 10)
    return arr


def separate_data(count, n, L):
    size = n * L // count
    indexs = []
    sizes = []
    ost = n * L - size * count
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

    n = int(namespace.sizes[0])
    m = int(namespace.sizes[1])
    L = int(namespace.sizes[2])
    count_threads = int(namespace.threads)
    first_matrix = create_matrix(n, m, False)
    second_matrix = create_matrix(m, L, False)
    result_matrix = create_matrix(n, L, True)
    print(first_matrix)
    print()
    print(second_matrix)
    transpose_second_matrix = transpose_matrix(second_matrix)
    print()
    print(transpose_second_matrix)
    print()
    procceses = []
    indexs, sizes = separate_data(count_threads, n, L)
    start_time = time.time()
    for i in range(count_threads):
        process = multiprocessing.Process(target=calculate_matrix,
                                  args=(indexs[i], sizes[i], first_matrix, transpose_second_matrix, result_matrix))
        procceses.append(process)
        process.start()
        #calculate_matrix(indexs[i], sizes[i], first_matrix, transpose_second_matrix, result_matrix)
    for process in procceses:
        process.join()
    print(indexs)
    print(sizes)
    print()
    print(result_matrix)
    print('seconds: ' + str(time.time() - start_time))

if __name__ == "__main__":
    main()
