from new_alpha import AI
from size6 import size6
ai =AI("player1",5)
size=size6(6)
size.board()
player="player1"
while sum(size.game[0:6]) != 0 and sum(size.game[7:13]) != 0:
    if ai.player == player:
        print("AI",player)
        move=ai.move_series(size)
        temps=size.game[move]
        size.game[move]=0
        result=size.movingforward(temps,move,"player1")
        if result[0]==1 and (result[2]!=6 and result[2]!=13):
            size.takeover(result[2],player)
        else:
            player="player2"
        size.board()
    else:
        player=size.play("player2")
        player = "player1"
size.winner()
    