#!/usr/bin/env python3

import sys
import matrix


if __name__ == "__main__":
    matrices = []
    for line in sys.stdin:
        matrices.append(matrix.read_row_col_data(line))

    # Transition matrix.
    T = matrices[0]
    # Emission matrix.
    E = matrices[1]
    # Initial state probability distribution.
    P = matrices[2]

    matrix.print_m(T)
    print()
    matrix.print_m(E)
    print()
    matrix.print_m(P)
    print()

    # Multiply transition matrix (T) with our current estimate of states (P).
    # P * T
    a = matrix.multiply(P, T)
    matrix.print_m(a)
