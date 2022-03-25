import csv
from new_alpha import AI
from size6 import size6
from time import time
import pickle
total_time=0

for x in range(0,2):
    ai =AI("player1",5)
    size=size6(6)
    size.board()
    player="player1"


    while sum(size.game[0:6]) != 0 and sum(size.game[7:13]) != 0:
        t = time()
        if ai.player == player:
            print("AI",player)
            move=ai.move_series(size)
            temps=size.game[move]
            size.game[move]=0
            result=size.movingforward(temps,move,"player1")
            print("Calculated in %.1fs" % (time() - t))
            total_time += time() - t
            if result[0]==1 and (result[2]!=6 and result[2]!=13):
                size.takeover(result[2],player)
            else:
                player="player2"
            size.board()
        else:
            player=size.play("player2")
            player = "player1"
    print("total time is %.1fs" % (total_time))
    #size.winner()

    with open('time.csv', 'w+', newline='') as csvfile:
        fieldnames = ['winner', 'total_time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        u=size.winner()
        writer.writerow({'winner': u, 'total_time': total_time})
