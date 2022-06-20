a = int(input("출력할 구구단을 입력하시오 "))

sum = 0

for i in range(1, 9+1):
    sum = a*i
    print("{} * {} = {}".format(a,i,sum))
