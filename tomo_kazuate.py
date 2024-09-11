# -*- coding: utf-8 -*-

#総合演習2　自由テーマ「HIT&BLOW」
#コンピューターがランダムで4桁の数(各桁0～9、重複なし)を考える。※0123等も含まれる。
#プレイヤーはその数を当てたら勝ち。
#プレイヤーが入力した数について、
#桁の位置と数字が同じだとHIT、桁は違うが数字が同じだとBLOW
#何回で当てられるかを競う。


import random             #random関数を使って0～9までの整数を（文字列扱い）を出す×4
num=["0","1","2","3","4","5","6","7","8","9"]
c0=random.choice(num)
num.remove(c0)
c1=random.choice(num)     #工夫点①
num.remove(c1)            #もともとは下のようにrandintで整数値を出していたが、
c2=random.choice(num)     #4つの数に重複なしというルールを知ったので
num.remove(c2)            #0～9を文字列扱いしてリストを作成、そこからchoiceで選ぶことに。
c3=random.choice(num)     #各次の行でリストnumからremoveすることで重複しないようにした。

com=[c0,c1,c2,c3]         #リストcomに入れる

#c1=random.randint(0,9)
#c2=random.randint(0,9)
#c3=random.randint(0,9)
#c0=str(c0)
#c1=str(c1)
#c2=str(c2)
#c3=str(c3)



k=0                       #何回で正解したかkでカウントする
h=0                       #HITの数を仮置き
b=0                       #BLOWの数を仮置き
ber=["0","1","2","3","4","5","6","7","8","9"]   #後述

while True:                                #正解するまで繰り返す
  while True:                              #半角4桁の数が入力されるまで繰り返す。
    x=str(input("半角4桁の数を入力:"))
    pla=list(x)
    if len(pla)==4 and pla[0] in ber and pla[1] in ber and pla[2] in ber and pla[3] in ber:
      break


#工夫点②
#初めは数字として4桁の数を扱っていたが、
#0123も答えとして扱う以上、数字としては扱うのが難しくなった。
#（エラー値の処理に困っていた。x=int(x) and x=>1111 andX=<9999 これだと0123ができない！）
#よって文字列に変換。リストplaを作成。
#len関数を用い、要素の数が4個、かつ、『入力した値が半角数字であるという条件』…（＊）で
#inputのエラー値をはじくことができた。

#ただ（＊）がそれぞれの数がber=["0","1","2","3","4","5","6","7","8","9"]のいずれかがどうか
#という判定方法はちょっとキモいやり方な気もする…。もっと適切で簡潔な方法はないのか？


  k+=1                          #回数をカウント


  if pla[0]==com[0]:            #まずはHITの処理。
    h+=1                        #リストplaとリストcomの同じ位置に同じ文字がある場合に
    pla[0]="a"                  #HITとしてカウント。

  if pla[1]==com[1]:            #工夫点③
    h+=1                        #HITした文字を一度違う文字で仮置きすることで、
    pla[1]="b"                  #このあとのBLOWでHITを2重カウントしないようにした。

  if pla[2]==com[2]:
    h+=1
    pla[2]="c"

  if pla[3]==com[3]:
    h+=1
    pla[3]="d"


  if pla[0] in com:             #次にBLOWの処理。
    if True:                    #リストplaのそれぞれの要素がリストcomに含まれているか
      b+=1                      #チェックして、含まれていたらBLOWとしてカウント
  if pla[1] in com:
    if True:
      b+=1
  if pla[2] in com:
    if True:
      b+=1
  if pla[3] in com:
    if True:
      b+=1

  print("Hit:{} Blow:{}".format(h,b))

  if h==4:                     #HITが4回カウントされたということはそれが正解。
    print("正解です！あなたは{}回で導きました。".format(k))
    break                      #正解したのでループ終了。

  h=0                          #工夫点④
  b=0                          #はじめ、この部分を書いておらず、
                               #1回目の試行のHITとBLOWが,2回目の試行のHITとBLOWの結果に
                               #加算されてしまっていた。
                               #h=0,b=0と置くことで、HITとBLOWの値をリセットした。
                               #ループによって一番上の while True: まで戻る。