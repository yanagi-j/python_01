class battle:
    def __init__(self,win,lose,tie):
        self.win = win
        self.lose = lose
        self.tie = tie

    def battle_vs(self):
        com_i = random.randint(1,999) % 3

        print("じゃーんけーん")
        input_lines = input()
        you_i = int(input_lines) % 3
        print("you=",you_i,"com=",com_i)
        if you_i == com_i:
            self.tie = self.tie + 1
#            print("あーいこーで")
        else:
            if (you_i == 0) and (com_i == 1):
                print("＼(*＾▽＾*)／")
                self.win = self.win + 1
            elif (you_i == 1) and (com_i == 2):
                print("＼(*＾▽＾*)／")
                self.win = self.win + 1
            elif (you_i == 2) and (com_i == 0):
                print("＼(*＾▽＾*)／")
                self.win = self.win + 1
            else:
                print("(×_×)")
                self.lose = self.lose + 1
#            print("じゃーんけーん")

win = 0
lose = 0
tie = 0

import sys
import random

wining = 3
print("先に",wining,"勝した方が勝ちです")
print("グー:0 チョキ:1 パー:2")

for i in range(1,100):
    myinstance = battle(win,lose,tie)
    myinstance.battle_vs()
    win = myinstance.win
    lose = myinstance.lose
    tie = myinstance.tie
    if win >= wining:
        print("あなたの勝ちです",win,"勝",lose,"敗")
        sys.exit()
    elif lose >= wining:
        print("あなたの負けです",win,"勝",lose,"敗")
        sys.exit()
