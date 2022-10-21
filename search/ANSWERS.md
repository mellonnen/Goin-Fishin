# Answers

## Q1

- Possible states
  Is all states that can be reached by a sequence of legal moves.

- Initial state $s_0$
  No time has passed, no fishes has been caught.

- Transition function
  A player either moves their hook up, down, or moves the boat left or right. Also, if a player stays in the same position.

## Q2

The time hits zero, Or there are no fishes left to catch.

## Q3

The function describes the difference in scores for the two players, a quantity we want to maximize

## Q4

In the terminal state the proposed heuristic perfectly describes the utility function.

## Q5

Imagine if player A has 6 points, and player B has 4 points. But, player B has hooked the last fish worth 3 points and is reeling it in. In that case the proposed heuristic will be positive for A right until player B gets the fish into the boat.

## Q6

We value all the opposing players transitions equally, you essentially assume that the opponent will play randomly.

Imagine there are two fishes worth 2 points each, we can choose to take either of them in a single move. Also let's assume that we are down a single point in the total score, and that our opponent can also take one of the fishes in the next move.

Using the proposed heuristic, we will evaluate both the fishes equally. But, if we take the fish that our opponent can not take in a single move, we will lose as our opponent will simply take the fish and win on points.
