import random
from size6 import size6
from matplotlib import pyplot as plt

class AI(object):
    def __init__(self,player=None, lookahead=None, relative_score = False, horde=False, relative_horde=False):
        self.player = player
        self.opponent = "player2" if self.player == "player1" else "player1"
        self.search_count=0
        self.board=None
        self.horde = horde
        self.lookahead = lookahead
        self.relative_score = relative_score
        self.relative_horde = relative_horde

    for x in range(3):
        def eval_heuristic(self, board):
            score = board.get_score(self.player)
            pieces = 0
            if self.horde:
                if self.relative_horde:
                    pieces = (pieces - board.get_pieces(self.opponent))
                else:
                    pieces = board.get_pieces(self.player)
            if self.relative_score:
                score = (score - board.get_score(self.opponent))

            # print("Eval: ", score + pieces)
            return score + pieces

        def alphabeta(self, board, alpha, beta, player, depth):
            value = 0
            self.search_count += 1
            if board.game_over() or depth <= 0:
                value = self.eval_heuristic(board)
            elif player == self.player:
                cut = False
                value = -1000
                i = 0
                while i < 6 and not cut:
                    board_copy = size6(6, other=board)
                    if board_copy.check_move(self.player, i):
                        temp = board_copy.game[i]
                        # board_copy.game[i]=0
                        next_player = board_copy.movingforward(board_copy.game[i], i, self.player)
                        value = max(value, self.alphabeta(board_copy, alpha, beta, self.player, depth - 1))
                        alpha = max(value, alpha)
                        if alpha >= beta:
                            cut = True
                    else:
                        alpha = -1000
                    i += 1
            else:
                cut = False
                value = 1000
                i = 0
                while i < 6 and not cut:
                    board_copy = size6(6, other=board)
                    if board_copy.check_move(self.opponent, i):
                        temp = board_copy.game[i]
                        # board_copy.game[i]=0
                        next_player = board_copy.movingforward(board_copy.game[i], i, self.player)
                        value = max(value, self.alphabeta(board_copy, alpha, beta, self.player, depth - 1))
                        alpha = max(value, alpha)
                        if alpha >= beta:
                            cut = True
                    else:
                        beta = 72
                    i += 1
            # print("from alpha-beta",value)
            return value

        def move_series(self, board):
            alpha = -1000
            beta = 1000
            value = alpha
            i = move = 0
            cut = False
            max_alpha = 0
            self.search_count = 0
            print("searching ..")
            while i < 6 and not cut:
                board_copy = size6(6, other=board)
                board_copy_arr = []
                if board_copy.check_move(self.player, i):
                    temp = board_copy.game[i]
                    # board_copy.game[i]=0
                    # print("this is borad_copy", board_copy.game)
                    board_copy.movingforward(board_copy.game[i], i, self.player)
                    value = max(value, self.alphabeta(board_copy, alpha, beta, self.player, self.lookahead))
                    alpha = max(value, alpha)
                    print("Current Board", board_copy.game[0:14])
                    if max_alpha <= alpha:
                        max_alpha = alpha
                        board_copy_arr = board_copy.game[0:14]

                    # print("alpha", alpha)
                    # print("value", value)
                    if alpha <= value:
                        alpha = value
                        move = i
                    if alpha >= beta:
                        cut = True
                i += 1

            print("value", value)
            print("Game Board", board_copy_arr[0:14])
            print("Searched", self.search_count, "possibilities")
            return move
