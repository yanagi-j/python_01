class battle:
    def __init__(self,i,hit,blw):
        self.i = i
        self.hit = hit
        self.blw = blw

    def battle_vs(self):
        print("あなた[",i,"/",cha,"]")
        while True:
            input_lines = input()
            input_str = str(input_lines)
            leng = len(input_str)
            lenu = len(sorted(set(input_str), key=input_str.index))
            if (leng == num)&(leng == lenu):
                #４けた、かつ重複が無い
                break
            print("もう一度")

        for j in range(0,num):
            if list[j] == input_str[j]:
                #同じ位置が一致
                self.hit = self.hit + 1
            else:
                #同じ位置が不一致
                for k in range(0,num):
                    if list[j] == input_str[k]:
                        #異なる位置が一致
                        self.blw = self.blw + 1
                        break
        print(self.hit,"hit ",self.blw,"blow")

import sys
import random

hit = 0
blw = 0
num = 3
cha = 15
print(num,"けたの数を当てるゲームです（",cha,"回勝負）")

# numけたの数字を作成
population=["0","1","2","3","4","5","6","7","8","9"]
list = random.sample(population,num)

for i in range(1,cha+1):
    myinstance = battle(i,hit,blw)
    myinstance.battle_vs()
    if myinstance.hit >= num:
        print("あなたの勝ちです",list)
        sys.exit()

print("あなたの負けです",list)
