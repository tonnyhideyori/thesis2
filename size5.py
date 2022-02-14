import random
class size5(object):
    def __init__(self,other=None):
        self.game=[6]*12
        self.game[5]=self.game[11]=0
        if other:
            for i in range(0,len(other.game)):
                self.game[i]=other.game[i]
        
    def board(self):
        x = self.game[6:11]
        x.reverse()
        print('\npit nos       :5  4  3  2  1')
        print('                -------------------')
        print('Player2 >>> ', [self.game[11]], "  ".join(map(str, x)))
        print('Player1 >>> ', '  ', self.game[0:5], [self.game[5]])
        print('                -------------------')
        print('pit nos       :  1  2  3  4  5')
        
    def takeover(self, x, player):
        if player == "player1" and self.game[8-x] > 0:
            self.game[5] = self.game[5]+self.game[10-x] + self.game[x]
            self.game[10-x] = self.game[x] = 0
        if player == "player2" and self.game[10-x] > 0:
            self.game[11] = self.game[11] + self.game[10-x] + self.game[x]
            self.game[10-x] = self.game[x] = 0
            
    def player(self, player):
        second = []
        #This is chosing a random postion just for the automation
        if player == "player1":
            player1Move = random.randint(0, 4)
            nonzero = [i for i, x in enumerate(
                self.game[0:5]) if x > 0 and self.game.index(x) < 5]
            while self.game[player1Move] == 0 and len(nonzero) > 0:
                player1Move = random.choice(nonzero)
            temp = self.game[player1Move]
            self.game[player1Move] = 0
        else:
            player1Move = random.randint(6, 10)
            nonzero = [i for i, x in enumerate(self.game) if x > 0]
            for i in nonzero:
                if i > 4 and i < 11:
                    second.append(i)
            while self.game[player1Move] == 0 and len(second) > 0:
                print("choose new position")
                player1Move = random.choice(second)
            temp = self.game[player1Move]
            self.game[player1Move] = 0
        return [temp, player1Move]

    def movingforward(self, count, player1, who):
        #how to move the token
        if who == "player1":
            step = 0
            while count > 0:
                step += 1
                try:
                    if (step+player1) % 11 == 0:
                        step += 1
                    self.game[step+player1] += 1
                    x = step+player1
                except:
                    self.game[(step+player1) % 11-1] += 1
                    x = (step+player1) % 11-1
                count -= 1
        else:
            step = 0
            while count > 0:
                step += 1
                try:
                    self.game[step+player1] += 1
                    x = step+player1
                except:
                    if (step+player1) % 11 == 6:
                        step += 1
                    self.game[(step+player1-1) % 11] += 1
                    x = (step+player1-1) % 11
                count -= 1
        return [self.game[x], player1, x]

    def play(self, player):
        # how to play self.game
        if player == "player1":
            outcome = self.player("player1")
        else:
            outcome = self.player("player2")
        result = self.movingforward(outcome[0], outcome[1], player)
        if result[0] == 1 and (result[2] != 5 and result[2] != 11):
            self.takeover(result[2], player)
        #while (player == "play1" and result[2] == 6) or (player == "play2" and result[2] == 13):
            #outcome=player1(player)
            #result = movingforward(outcome[0], outcome[1], player)
            #if result[0]==1 and (result[2]!=6 and result[2]!=13):
            #    takeover(result[2],player)
        print(player)
        self.board()
        return player
    
    def simulate(self):
        self.board()
    #iteration of the game until one of the player have zero token
        x = self.play("player1")
        self.board()
        while sum(self.game[0:5]) != 0 and sum(self.game[6:11]) != 0:  # checking if you don
            if x == "player1":
                x = self.play("player2")
            else:
                x = self.play("player1")

    def winner(self):
        if sum(self.game[0:5]) > sum(self.game[6:12]):
            winner = "player 1"
        else:
            winner = "player 2"
        print("The winner is :", winner)
