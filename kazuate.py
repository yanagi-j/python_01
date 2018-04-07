print(" 数字と場所が一致するとhit,数字のみの一致だとblow")
print(" 「千」に千の位を、「百」に百の位を、｢十｣に十の位を、｢一｣に一の位を書いて下さい")
print("　※千の位に０は無し、同じ数字は２つ以上無い")

import random

A=random.randint(1,9)
while True:
    B=random.randint(0,9)
    if A!=B:
        break
while True:
    C=random.randint(0,9)
    if A!=C and B!=C:
        break
while True:
    D=random.randint(0,9)
    if A!=D and B!=D and C!=D:
        break

#print(A,B,C,D)

for i in range(15):
    input_line=input("千")
    a=int(input_line)
    input_line=input("百")
    b=int(input_line)
    input_line=input("十")
    c=int(input_line)
    input_line=input("一")
    d=int(input_line)

    hit=0
    blow=0

    if A==a:
        hit=hit+1
    if B==b:
        hit=hit+1
    if C==c:
        hit=hit+1
    if D==d:
        hit=hit+1

    if B==a or C==a or D==a:
        blow=blow+1
    if A==b or C==b or D==b:
        blow=blow+1
    if A==c or B==c or D==c:
        blow=blow+1
    if A==d or B==d or C==d:
        blow=blow+1

    print("hit=",hit,"blow=",blow)

    if hit==4:
        print("あなたの勝ちです")
        exit()

print("あなたの負けです")
exit()
