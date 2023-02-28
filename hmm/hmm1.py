#!/usr/bin/env pypy3

import sys
import matrix


if __name__ == "__main__":
    # First three lines are transition, emission and initial state probability matrices.
    # The last line is a 1xN matrix representing the sequence of emissions.
    matrices = []
    for line in sys.stdin:
        if len(matrices) < 3:
            matrices.append(matrix.read_row_col_data(line))
        else:
            # 1xN matrix of the sequence of emissions.
            seq = line.split()
            matrices.append(seq[1:])

    # Transition matrix.
    T = matrices[0]
    # Emission matrix.
    E = matrices[1]
    # Initial state probability distribution.
    P = matrices[2]

    # Sequence of emissions.
    S = matrices[3]

    # Multiply transition matrix (T) with our current estimate of states (P).
    # P * T
    P_x_T = matrix.multiply(P, T)

    # Multiply result matrix (PxT) with the observation matrix (E).
    # This gives us the next emission probability matrix.
    # PxT * E
    PxT_x_E = matrix.multiply(P_x_T, E)

    matrix.print_m(S)
