import random
game=[6]*14
game[6]=game[13]=0
def board():
    x=game[7:13]
    x.reverse()
    print('\npit nos       :  6  5  4  3  2  1')
    print('                -------------------')
    print('Player2 >>> ',[game[13]], "  ".join(map(str,x)))
    print('Player1 >>> ', '  ', game[0:6], [game[6]])
    print('                -------------------')
    print('pit nos       :  1  2  3  4  5  6')

def takeover(x,player):
    if player == "play1" and game[12-x] > 0:
        game[6]=game[6]+game[12-x] + game[x]
        game[12-x]=game[x]=0
    if player=="play2" and game[12-x]>0:
        game[13]=game[13] + game[12-x] + game[x]
        game[12-x] = game[x] = 0

def player1(player):
    second=[]
    #This is chosing a random postion just for the automation
    if player=="play1":
        player1Move=random.randint(0,5)
        nonzero = [i for i, x in enumerate(game[0:6]) if x > 0 and game.index(x) < 6]
        #print(f"nonzero :{nonzero}")
        while game[player1Move]==0 and len(nonzero)>0:
            player1Move = random.choice(nonzero)
        temp = game[player1Move]
        game[player1Move]=0
    else:
        player1Move = random.randint(7, 12)
        nonzero = [i for i, x in enumerate(game) if x > 0]
        for i in nonzero:
            if i >6 and i<13:
                second.append(i)
        #print("second nonzero ", player, nonzero)
        while game[player1Move] == 0 and len(second) > 0:
            print("choose new position")
            player1Move = random.choice(second)
        temp = game[player1Move]
        game[player1Move] = 0
    return [temp,player1Move]


def movingforward(count,player1,who):
    #this is the actual game how to move tokes so play1 and play2 have same principle except on index and home store play1 avoid index 13 and play2 avoid index 6
    # i use modulo when token is above 13 but I have another idea that we can use two lists one for each and when we know we are out index we move to the other list . when iterate until we heat zero count(stones at hand) i think two list will much easier with the implementation of try and except.
    if who=="play1":
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
    return [game[x],player1,x]
def play(player):
    # how to play game
    if player=="play1":
        outcome=player1("play1")
    else:
        outcome=player1("play2")
    result=movingforward(outcome[0],outcome[1],player)
    if result[0]==1 and (result[2]!=6 and result[2]!=13):
        takeover(result[2],player)
    board()
    return player

def simulate():
    board()
    #iteration of the game until one of the player have zero token
    x=play("play1")
    while sum(game[0:6])!=0 and sum(game[7:13])!=0:
        if x=="play1":
             x=play("play2")
        else:
            x=play("play1")
simulate()
