class AlphaBeta(object):
    def basic_alphabeta(self,board,alpha,beta,player,depth):
        if board.game_over() or depth == 0:
            value = board.get_pieces(player) + board.get_score(player)
            return value
        if player == "player1":
            value = -72
            cut=False
            for i in range(0,(len(board.game))/2):
                if not cut: 
                    next_player="player2" if player == "player1" else "player1"
                    value =max(value, self.basic_alphabeta(board,alpha,beta,next_player,depth-1))
                    beta=max(beta,value)
                    if alpha>=beta:
                        cut = True
                    else:
                        alpha = -72
        else:
            value = 72
            cut = False
            for i in range((len(board.game))/2, len(board.game)):
                if not cut: 
                    next_player="player1" if player == "player2" else "player2"
                    value =min(value, self.basic_alphabeta(board,alpha,beta,next_player,depth-1))
                    beta = min(beta, value)
                    if alpha >= beta:
                        cut = True
                    else:
                        beta = 72
        return value
    def evaluate(self,board):
        return sum(board[0:7]) - sum(board[7:14])
    
    def children(self,board,player):
        root=[]
        copy_board=board
        #checking possible moves.
        if player == "player1":
            nonzero = [i for i, x in enumerate(copy_board[0:6]) if x > 0 and copy_board.index(x) < 6]
        else:
            nonzero = [i for i, x in enumerate(copy_board[7:13]) if x > 0 and copy_board.index(x) < 13]
        for none in nonzero:
            print("trying to find none",none)
            child=self.movingforward(copy_board,copy_board[none],none,player)
            root.append(child)
        return root
            
    
    def alphabeta(self,board,alpha,beta,player,depth):
        if (sum(board[0:6]) == 0 or sum(board[7:13]) == 0) or depth == 0:
            bestvalue = self.evaluate(board)
            print("this is best value",bestvalue)
            return bestvalue
        elif player=="player1":
            opponent ="player2"
            bestvalue = -72
            children = self.children(board,player)
            for child in children:
                print(child)
                value = self.alphabeta(child,alpha,beta,opponent,depth-1)
                print("this is value",value)
                bestvalue = max(bestvalue,value)
                alpha = max(alpha,bestvalue)
                if alpha >= beta:
                    break
        else:
            opponent = "player1"
            bestvalue = 72
            children = self.children(board,player)
            for child in children:
                value = self.alphabeta(child,alpha,beta,opponent,depth-1)
                bestvalue = min(bestvalue,value)
                beta = min(beta,bestvalue)
                if alpha >= beta:
                    break

    def movealphabeta(self,board):
        copy=board
        value=alpha=-72
        beta=72
        player="player1"
        i=move=0
        while i < 6:
            if board[i] !=0:
                value = max(value, self.alphabeta(copy, alpha, beta, player, 6))
                if alpha < value:
                    alpha = value
                    move = i
                if alpha >= beta:
                        break
            i+=1
        return [board[move],move]
    
    def movingforward(self,game,count,player1,who):
        #how to move the token
        if who=="player1":
            step=0
            while count > 0:
                step+=1
                try:
                    if (step+player1)%13==0:
                        step+=1
                    game[step+player1]+=1
                    x=step+player1
                except:
                    game[(step+player1) % 13-1] += 1
                    x=(step+player1)%13-1
                count -= 1
        else:
            step = 0
            while count > 0 :
                step += 1
                try:
                    game[step+player1]+=1
                    x=step+player1
                except:
                    if (step+player1)%13 == 7:
                        step += 1
                    game[(step+player1-1)%13]+=1
                    x = (step+player1-1)%13
                count -= 1
        return game