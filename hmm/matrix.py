from itertools import starmap
from operator import mul


# from https://stackoverflow.com/a/45159105/2591460
def multiply(a, b):
    return [[sum(starmap(mul, zip(row, col))) for col in zip(*b)] for row in a]


def create(num_rows, num_cols, data):
    matrix = []
    for row in range(num_rows):
        matrix.append([])
        for col in range(num_cols):
            row_offset = row * num_cols
            matrix[row].append(data[row_offset + col])
    return matrix


def print_m(matrix):
    for row in matrix:
        print("\t".join(map(str, row)))


def read_row_col_data(line):
    nums = line.split()
    num_rows = nums[0]
    num_cols = nums[1]
    data = [float(x) for x in nums[2:]]

    m = create(int(num_rows), int(num_cols), data)
    return m
