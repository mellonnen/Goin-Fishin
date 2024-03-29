#!/usr/bin/env pypy3

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

    """
    print("T")
    matrix.print_m(T)
    print()
    print("E")
    matrix.print_m(E)
    print()
    print("P")
    matrix.print_m(P)
    print()
    """
    # Multiply transition matrix (T) with our current estimate of states (P).
    # P * T
    P_x_T = matrix.multiply(P, T)

    """
    print("P x T")
    matrix.print_m(P_x_T)
    print()
    """

    # Multiply result matrix (PxT) with the observation matrix (E).
    # PxT * E
    PxT_x_E = matrix.multiply(P_x_T, E)

    """
    print("(P x T) x E")
    matrix.print_m(PxT_x_E)
    print()
    """

    matrix.print_output(PxT_x_E)
