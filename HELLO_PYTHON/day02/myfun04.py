def addminmuldiv(a, b):
    return a+b, a-b, a*b, a/b


add, min, mul, div = addminmuldiv(1, 6)


print("add", add)
print("min", min)
print("mul", mul)
print("div", div)

sum = addminmuldiv(5,10)

print(sum)
