a = int(input("첫번째 수를 입력하시오 "))
b = int(input("두번째 수를 입력하시오 "))

sum = 0

for i in range(a, b+1):
    sum += i


print(str(a)+"에서", str(b)+"의 합은", str(sum)+"입니다.")
