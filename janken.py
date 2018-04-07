win =0
los =0

import random

print("グーなら０、チョキなら１、パーなら２　３勝したら勝ちです")

while (win<3)and(los<3):
    input_line=input()
    you=int(input_line)%3

    com=random.randint(0,2)
    print("com=",com)

    if com==you:
        print("あいこ")
    else:
        if (com==0)and(you==2):
            win=win+1
        elif (com==2)and(you==1):
            win=win+1
        elif (com==1)and(you==0):
            win=win+1
        else:
            los=los+1
    print(win,"勝",los,"敗")
#print(win,los)

if win>=3:
    print("あなたの勝ちです")
else:
    print("あなたの負けです")
