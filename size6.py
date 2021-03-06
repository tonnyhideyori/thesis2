import csv
import random
#from my_alphabeta import AlphaBeta
class size6(object):
    def __init__(self,seed,other=None):
        self.game = [seed]*14
        self.game[seed] = self.game[13] = 0
        if other != None:
            for i in range(0,len(other.game)):
                self.game[i]=other.game[i]

    
    def get_score(self,player):
        if player == "player1":
            return sum(self.game[0:6])
        else:
            return sum(self.game[7:])
        print(self,player)
    
    def get_piece(self,player):
        if player == "player1":
            return sum(self.game[0:6])
        else:
            return sum(self.game[7:13])
    def check_move(self,player,move):
        if player == "player1":
            if self.game[move]>0:
                return True
            else:
                return False
        else:
            if self.game[move]>0:
                return True
            else:
                return False

        
    def board(self):
        x=self.game[7:13]
        x.reverse()
        print('\npit nos       :  6  5  4  3  2  1')
        print('                -------------------')
        print('Player2 >>> ',[self.game[13]], "  ".join(map(str,x)))
        print('Player1 >>> ', '  ', self.game[0:6], [self.game[6]])
        print('                -------------------')
        print('pit nos       :  1  2  3  4  5  6')

    def takeover(self,x,player):
        if player == "player1" and self.game[12-x] > 0:
            self.game[6]=self.game[6]+self.game[12-x] + self.game[x]
            self.game[12-x]=self.game[x]=0
        if player=="player2" and self.game[12-x]>0:
            self.game[13]=self.game[13] + self.game[12-x] + self.game[x]
            self.game[12-x] = self.game[x] = 0

    def player(self,player):
        second=[]
        #This is chosing a random postion just for the automation
        if player=="player1":
            player1Move=random.randint(0,5)
            nonzero = [i for i, x in enumerate(self.game[0:6]) if x > 0 and self.game.index(x) < 6]
            while self.game[player1Move]==0 and len(nonzero)>0:
                player1Move = random.choice(nonzero)
            temp = self.game[player1Move]
            self.game[player1Move]=0
        else:
            player1Move = random.randint(7, 12)
            nonzero = [i for i, x in enumerate(self.game) if x > 0]
            for i in nonzero:
                if i >6 and i<13:
                    second.append(i)
            while self.game[player1Move] == 0 and len(second) > 0:
                print("choose new position")
                player1Move = random.choice(second)
            temp = self.game[player1Move]
            self.game[player1Move] = 0
        return [temp,player1Move]

    def movingforward(self,count,player1,who):
        #how to move the token
        if who=="player1":
            step=0
            while count > 0:
                step+=1
                try:
                    if (step+player1)%13==0:
                        step+=1
                    self.game[step+player1]+=1
                    x=step+player1
                except:
                    self.game[(step+player1) % 13-1] += 1
                    x=(step+player1)%13-1
                count -= 1
        else:
            step = 0
            while count > 0 :
                step += 1
                try:
                    self.game[step+player1]+=1
                    x=step+player1
                except:
                    if (step+player1)%13 == 7:
                        step += 1
                    self.game[(step+player1-1)%13]+=1
                    x = (step+player1-1)%13
                count -= 1
        return [self.game[x],player1,x]

    def play(self,player):
        #alpha=AlphaBeta()
        # how to play self.game
        #if player=="player1":
            #outcome=self.player("player1")#alpha.movealphabeta(self.game)#
        #else:
        outcome=self.player("player2")
        result=self.movingforward(outcome[0],outcome[1],player)
        if result[0]==1 and (result[2]!=6 and result[2]!=13):
            self.takeover(result[2],player)
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
        while sum(self.game[0:6]) != 0 and sum(self.game[7:13]) != 0:  # checking if you don
            if x == "player1":
                x = self.play("player2")
            else:
                x = self.play("player1")

    def winner(self):
        if sum(self.game[0:7]) > sum(self.game[7:14]):
            winner = "player 1"
        else:
            winner = "player 2"
        print("The winner is :", winner)
        return winner


    
    def game_over(self):
        return (sum(self.game[0:6]) == 0 or sum(self.game[7:13]) == 0)

    with open('time.csv', 'w') as csvfile:
        fieldnames = ['winner', 'total_time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'winner': winner})
        csvfile.close()


