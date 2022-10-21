#!/usr/bin/env python3
import random
import math

from fishing_game_core.game_tree import Node
from fishing_game_core.player_utils import PlayerController
from fishing_game_core.shared import ACTION_TO_STR


class PlayerControllerHuman(PlayerController):
    def player_loop(self):
        """
        Function that generates the loop of the game. In each iteration
        the human plays through the keyboard and send
        this to the game through the sender. Then it receives an
        update of the game through receiver, with this it computes the
        next movement.
        :return:
        """

        while True:
            # send message to game that you are ready
            msg = self.receiver()
            if msg["game_over"]:
                return


class PlayerControllerMinimax(PlayerController):
    def __init__(self):
        super(PlayerControllerMinimax, self).__init__()

    def player_loop(self):
        """
        Main loop for the minimax next move search.
        :return:
        """

        # Generate first message (Do not remove this line!)
        first_msg = self.receiver()

        while True:
            msg = self.receiver()

            # Create the root node of the game tree
            node = Node(message=msg, player=0)

            # Possible next moves: "stay", "left", "right", "up", "down"
            best_move = self.search_best_next_move(initial_tree_node=node)

            # Execute next action
            self.sender({"action": best_move, "search_time": None})

    def heuristic(self, node: Node):
        a_score, b_score = node.state.get_player_scores()
        return a_score - b_score

    def search_best_next_move(self, node: Node):
        """
        Use minimax (and extensions) to find best possible next move for player 0 (green boat)
        :param node: Initial game tree node
        :type node: game_tree.Node
            (see the Node class in game_tree.py for more information!)
        :return: either "stay", "left", "right", "up" or "down"
        :rtype: str
        """

        node.compute_and_get_children()

        if len(node.state.get_fish_positions()) == 0:
            return heuristic(node)
        else:
            # green boat
            if node.player == 0:
                best_possible = -math.inf
                for child in node.children:
                    v = search_best_next_move(child)
                    best_possible = max(best_possible, v)
                return best_possible
            # red boat
            else:
                best_possible = math.inf
                for child in node.children:
                    v = search_best_next_move(child)
                    best_possible = min(best_possible, v)
                return best_possible

        random_move = random.randrange(5)
        return ACTION_TO_STR[random_move]
