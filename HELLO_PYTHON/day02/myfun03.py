from random import random


def getHollJJak():
    if 0.5>random():
        return "홀"
    else :
        return "짝"

com = getHollJJak()
print("com", com)