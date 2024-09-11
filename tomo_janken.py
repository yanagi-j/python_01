#!/usr/bin/env python
# coding: utf-8

# In[17]:


#総合演習　問題1　じゃんけんゲーム
import random
list=["グー","チョキ","パー"]
com=random.choice(list)
win=0
lose=0
draw=0

while True:
  k=int(input("何回じゃんけんする？"))
  if k==int(k) and k>0:
    break

print("グーは0,チョキは2,パーは5だよ")

for i in range(k):
  while True:
    pla=int(input("0,2,5のいずれかを入力してね"))
    if pla==0 or pla==2 or pla==5:
      break
    else:
      k+=1

  if pla==0:
    pla="グー"
    print("あなた：グー")
    print("相手：{}".format(com))
  elif pla==2:
    pla="チョキ"
    print("あなた：チョキ")
    print("相手：{}".format(com))
  elif pla==5:
    pla="パー"
    print("あなた：パー")
    print("相手：{}".format(com))


  if pla==com:
    print("あいこ！")
    draw+=1
  elif pla=="グー":
    if com=="チョキ":
      print("あなたの勝ち！")
      win+=1
    elif com=="パー":
      print("あなたの負け！")
      lose+=1
  elif pla=="チョキ":
    if com=="パー":
      print("あなたの勝ち！")
      win+=1
    elif com=="グー":
      print("あなたの負け！")
      lose+=1
  elif pla=="パー":
    if com=="グー":
      print("あなたの勝ち！")
      win+=1
    elif com=="チョキ":
      print("あなたの負け！")
      lose+=1

coun=win+lose+draw
print("結果：{}戦中、勝ち{}回、負け{}回、引き分け{}回".format(coun,win,lose,draw))

