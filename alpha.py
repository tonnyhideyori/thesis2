import multiprocessing
import random
import sys
class Alpha(object):
    def __init__(self,player,lookforward,relative_score=False,evaluate=False,relative_evaluate=False):
        self.player = player
        self.opponent= "play1" if self.player == "play2" else "play2"
        self.search_count = 0
        self.lookforward = lookforward
        self.board = None
        self.evaluate = evaluate
        self.relative_score = relative_score
        self.relative_evaluate = relative_evaluate
    
    def eval_heuristic(self,board):
        score = board.get_score(self.player)
        pieces = 0
        if self.evaluate:
            if self.relative_evaluate:
                pieces = pieces - board.get_pieces(self.opponent)
            else:
                pieces = board.get_pieces(self.player)
        if self.relative_score:
            score = score - board.get_score(self.opponent)
        return score + pieces

    def alphabeta(self, board, alpha, beta, player, depth):
        value = 0
        self.search_count += 1
        if board.game_over() or depth == 0:
            value = self.eval_heuristic(board)
        elif player == self.player:
            cut = False
            value = -72
            i = 0
            while i <  6 and not cut:
                board_copy = Board(board) # old game or new game not like this
                if board_copy.check_move(self.player,i): # I should use function player with input player
                    next_player=board_copy.check_move(self.player,i) # I should use function player with input player
                    value = max(value,self.alphabeta(board_copy,alpha,beta,next_player,depth-1))
                    alpha=min(value,alpha)
                    if alpha >= beta:
                        cut = True
                    else: #no moves:
                        beta = -72
                i += 1
        else:  # opponent
            cut = False
            value = 72
            i = 0
            # for each opponent move, check if its valid, if so get the value of the next possible move
            while i < 6 and not cut:
                board_copy = Board(board)
                # if i is a valid move
                if board_copy.check_move(self.opponent, i):
                        next_player = board_copy.move(self.opponent, i)
                        value = min(value, self.alphabeta(
                            board_copy, alpha, beta, next_player, depth-1))
                        beta = min(value, beta)
                        if alpha >= beta:
                            cut = True
                else:  # no moves
                    beta = 72
                i += 1
        return value       
    
    def get_move_score(self, move):
        value = -50
        board_copy = Board(self.board)
        next_player = self.player
	# repeats are prioritized by increasing score
        while next_player == self.player and board_copy.check_move(self.player, move):
            next_player = board_copy.move(self.player, move) # change the function name to our function
			# if the next player has no move, change to other player
            if not board_copy.has_move(self.player):
                next_player = (next_player+1) % 2 # I have to change this to select player
                value = max(value, self.alphabeta(board_copy, -72, 72, next_player, self.lookforward))

        return value
    
    def move_parallel(self, board):
        move = 0
		#print 'AI Thinking...'
        try:
            pool = multiprocessing.Pool(multiprocessing.cpu_count())		
            move = 0		
            self.board = board
            # map all possible plays to unpack
            scores = pool.map_async(self.unpack_get_move_score, [(self,0), (self,1), (self,2), (self,3), (self,4), (self,5)]).get(60)	
            scores = list(scores)			
            # allow keyboard intteruptions 
            for i in range(0, 6): # ignore first move, already chosen
                if scores[move] < scores[i]:
                    move = i
        except KeyboardInterrupt:
            pool.terminate()
            sys.exit(-1)
        finally:
            pool.close()		
        pool.join()
        return move
    
    def move_serial(self, board):
        alpha = -48
        beta = 48
        value = alpha
        i = move = 0
        # foreach move possible
        cut = False
        self.search_count = 0
        print('AI thinking')
        # for each move, check if its valid, if so get the value of the next possible move
        while i < 6 and not cut:
            board_copy = Board(board)
            # if i is a valid move, else ignore
            if board_copy.check_move(self.player, i): 
                next_player = board_copy.move(self.player, i)
                # if the next player has no move, change to other player
                if not board_copy.has_move(self.player):
                    next_player = (next_player+1)%2
                # get next max move
                value = max(value, self.alphabeta(board_copy, alpha, beta, next_player, self.lookahead))
                if alpha < value:
                    alpha = value
                    move = i
                if alpha > beta:
                    cut = True
            i+=1
        print(f'Searched  {self.search_count}  possibilities')
        return move

    def move(self, board, parallel):
        if parallel:
            return self.move_parallel(board)
        else:
            return self.move_serial(board)
    
    
# unpack the async map args , expecting (ai_obj, move)
    def unpack_get_move_score(self,args):
        score = args[0].get_move_score(args[1])
        return score


def get_state_space(board, player, depth):
	count = 0
	if not board.game_over() and depth > 0:
		moves = []  # [(board,player) ,	...]
		# search siblings
		for i in range(0, 6):
			if board.check_move(player, i):
				count += 1
				board_copy = Board(board)
				next_player = board_copy.move(player, i)
				moves.append((board_copy, next_player))
		# search sibling children
		for move in moves:
			count += get_state_space(move[0], move[1], depth-1)
	return count
