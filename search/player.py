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
            best_move = 0
            for max_depth in range (1, 5):
                _, best_move = self.search_best_next_move(node, max_depth)

            # Execute next action
            self.sender({"action": ACTION_TO_STR[best_move], "search_time": None})

    def heuristic(self, node: Node):
        a_score, b_score = node.state.get_player_scores()
        return a_score - b_score

    def search_best_next_move(self, node: Node, depth: int):
        """
        Use minimax (and extensions) to find best possible next move for player 0 (green boat)
        :param node: Initial game tree node
        :type node: game_tree.Node
            (see the Node class in game_tree.py for more information!)
        :return: either "stay", "left", "right", "up" or "down"
        :rtype: str
        """

        node.compute_and_get_children()

        if depth == 0 or len(node.state.get_fish_positions()) == 0:
            return self.heuristic(node), None
            # green boat
        if node.state.get_player() == 0:
            best_possible = -math.inf
            best_move = 0
            for child in node.children:
                v, _ = self.search_best_next_move(child, depth-1)
                if best_possible < v:
                    best_possible = v
                    best_move = child.move
            return best_possible, best_move
        # red boat
        else:
            best_possible = math.inf
            best_move = 0
            for child in node.children:
                v, _ = self.search_best_next_move(child, depth-1)
                if best_possible > v:
                    best_possible = v
                    best_move = child.move
            return best_possible, best_move

        # random_move = random.randrange(5)
        # return ACTION_TO_STR[random_move]
