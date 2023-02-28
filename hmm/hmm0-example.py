#!/usr/bin/env python3
#
#

# Selecting any coin has the probability of 0.5 at each step.
pi = [0.5, 0.5]


# Transition probability matrix. Shows the probability of transitioning
# from coin C1 to C2 and vice-versa. All transitions have probability 0.5.
#       C1            C2
# C1    P(C1 | C1)    P(C2 | C1)
# C2    P(C1 | C2)    P(C2 | C2)
A = [[0.5, 0.5], [0.5, 0.5]]


# Observation probability matrix. Shows the probability of observing
# a certain outcome (H or T) given a certain coin (C1 or C2).
#       H            T
# C1    P(H | C1)    P(T | C1)
# C2    P(H | C2)    P(T | C2)
A = [[0.5, 0.5], [0.5, 0.5]]
