from size7 import size7
from size8 import size8
from size6 import size6
from size5 import size5
from size4 import size4
print("please choose number of seeds")
seed=int(input())
print("please choose number of pit (4,5,6,7,8)")
pit=int(input())
if pit==4:
    size=size4(seed)
    size.simulate()
    size.winner()
elif pit==5:
    size=size5()#seed)
    size.simulate()
    size.winner()
elif pit==6:
    size=size6(seed)
    size.simulate()
    size.winner()
elif pit==7:
    size=size7(seed)
    size.simulate()
    size.winner()
else:
    size=size8(seed)
    size.simulate()
    size.winner()
