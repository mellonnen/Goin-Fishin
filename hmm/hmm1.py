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
            seq = list(map(int, line.split()))
            matrices.append(seq[1:])

    # Transition matrix.
    T = matrices[0]
    # Emission matrix.
    B = matrices[1]
    # Initial state probability distribution.
    P = matrices[2]
    # Sequence of emissions.
    S = matrices[3]

    N_hidden_states = len(P[0])
    N_time_steps = len(S)

    # alpha_ts contains alpha values for each time step, t. Every outer index is a time step t,
    # and the arrays contain the alpha values (i.e. probabilities of being in each of the hidden states) of that time step.
    alpha_ts = [[] for _ in range(N_time_steps)]
    for i in range(N_hidden_states):
        o1 = S[0]
        piᵢ = P[0][i]
        bᵢ_o1 = B[i][o1]
        alpha_1 = bᵢ_o1 * piᵢ
        alpha_ts[0].append(alpha_1)

    # with alpha_1 initialized, calculate the rest.
    for t in range(1, N_time_steps):
        for j in range(N_hidden_states):
            oₜ = S[t]
            bᵢ_oₜ = B[j][oₜ]
            # marginalize over the probability of having been in any other state at t − 1
            marginalized_probability = sum(
                (alpha_ts[t - 1][i] * T[i][j] * bᵢ_oₜ) for i in range(N_hidden_states)
            )
            alpha_ts[t].append(marginalized_probability)

    probability = sum((alpha_ts[N_time_steps - 1][h]) for h in range(N_hidden_states))
    print(probability)
