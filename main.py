import random
# setting of the Kalah board with 6 pits and 6 counters
player1 = [6, 6, 6, 6, 6, 6, 0]
player2 = [6, 6, 6, 6, 6, 6, 0]


print(" GAME OF KALAH")
print("_________________")

#illustration of the board where the 2nd player's pit numbers are reversed to mirror the board from 1st player's perspective.
#kalah pits are the ones with seperated single-values.
def board():
    player2.reverse()
    print('\npit nos       :  6  5  4  3  2  1')
    print('                -------------------')
    print('Player2 >>>', player2[:1], player2[1:7])
    print('Player1 >>> ', '  ', player1[0:6],player1[6:])
    print('                -------------------')
    print('pit nos       :  1  2  3  4  5  6')
    player2.reverse()

board()
def aut():
    Player1InGame = sum(player1[:6]) #or
    Player2InGame = sum(player2[:6])
    #to find out the number of counters each player has got in the pit which is non empty and initiate player 1 turn.
    while (Player1InGame != 0) or (Player2InGame != 0):
        # random.randint(1,6)#int(input('\nYOUR TURN, PLAYER 1!'))
        Player1Move = random.choice([1,2, 3, 4, 5, 6])
        Counters = player1[Player1Move - 1]
        if Counters == 0:
            print('NO COUNTERS IN THE PIT.\nTRY AGAIN\n')
            while Counters == 0:
                Player1Move = random.choice([1, 2, 3, 4, 5, 6])
                Counters = player1[Player1Move - 1]
            #continue
        # Check whether counters will flow into Player2's pits and distribute accordingly, or repeat turn if counters end in capture.
        if Counters + Player1Move < 7:
            player1[Player1Move - 1] = 0 #where you took th token
            for i in range(Player1Move, Counters+Player1Move):
                player1[i] = player1[i] + 1
            while player1[i]==1 and i!=6:
                player1[i] = player1[i]+player2[5-i]
                player2[5-i]=0
                
                Counters = player1[i]

                pass
            board()
        if Counters + Player1Move == 7:
            player1[Player1Move - 1] = 0
            for i in range(Player1Move, Counters+Player1Move):
                player1[i] = player1[i] + 1
            board()
            continue
        else:
            print('OF')
            OFlow = Counters + Player1Move - 6

            for i in range(Player1Move, 7):
                player1[i] = player1[i] + 1
            if OFlow < 7:
                player1[Player1Move - 1] = 0
                for i in range(0,OFlow-1):
                    player2[i] = player2[i] + 1
                board()
            # This handles overflow back into Player1's pits for large amount of counters.
            else:
                player1[Player1Move - 1] = 0
                for i in range(0, 5):
                    player2[i] = player2[i] + 1
                print("OFlow top"+str(OFlow))
                for i in range(0,OFlow-7):
                    print(i)
                    player1[i] = player1[i] + 1
                if (player1[i] == 1) and (i != 6):
                    player1[i] = player1[i] + player2[5-i]
                    player2[5-i] = 0
                    pass
                board()

        Player1InGame = sum(player1[:6])
        Player2InGame = sum(player2[:6])
        # Initiate player 2 turn. Structured the same as player 1 turn.
        while (Player1InGame != 0) and (Player2InGame != 0):
            # int(input('\nYOUR TURN, PLAYER 1!'))#int(input('\nYOUR TURN, PLAYER 2!'))
            Player2Move = random.choice([0,1,2,3,4])
            Counters = player2[Player2Move - 1]
            if player2[Player2Move - 1] == 0:
                print('NO COUNTERS.\nTRY AGAIN\n')
                continue
            elif Counters + Player2Move < 7:
                player2[Player2Move - 1] = 0
                for i in range(Player2Move, Counters+Player2Move):
                    player2[i] = player2[i] + 1
                if (player2[i] == 1) and (i != 6):
                    player2[i] = player2[i] + player1[5-i]
                    player1[5-i] = 0
                    pass
                board()
            elif Counters + Player2Move == 7:
                player2[Player2Move - 1] = 0
                for i in range(Player2Move, Counters+Player2Move):
                    player2[i] = player2[i] + 1
                board()
                continue
            else:
                print('OF')
                OFlow = Counters + Player2Move - 6
                for i in range(Player2Move, 7):
                    player2[i] = player2[i] + 1
                if OFlow < 7:
                    player2[Player2Move - 1] = 0
                    for i in range(0,OFlow-1):
                        player1[i] = player1[i] + 1

                else:
                    player2[Player2Move - 1] = 0
                    for i in range(0, 5):
                        player1[i] = player1[i] + 1
                    print("oflow"+str(OFlow))
                    for i in range(0, OFlow - 5):
                        player2[i] = player2[i] + 1
                    if (player2[i] == 1) and (i != 6):
                        player2[i] = player2[i] + player1[5-i]
                        player1[5-i] = 0
                        pass
                board()
                Player1InGame = sum(player1[:6])
                Player2InGame = sum(player2[:6])
            break


    print ('\nGAME OVER. \nPlayer 1 Scored: ', player1[6], '\nPlayer 2 Scored: ', player2[6])
    
aut()