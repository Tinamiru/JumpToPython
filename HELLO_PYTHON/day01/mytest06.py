from random import random
from secrets import choice

me = input("홀/짝을 입력해라 ")

if((me != "홀") and (me != "짝")):
    print("홀/짝만 입력하라요")
else:
    com = "홀", "짝"

    comooe = choice(com)

    print("나의 선택 : ", me)
    print("컴의 선택 : ", comooe)

    if(me == comooe):
        print("내가 이김")
    else:
        print("내가 짐")
