arr = [0, 1, 3, 1, 1, 1, 2, 2, 2, 2]

bicNum = max(arr)
index = arr.index(bicNum)

print("fucntion = ", index)

max = -1
for i in arr:
    if max < i:
        max = i
print("max = ", max)

myidx = -1
for i, data in enumerate(arr):
    if max == data:
        myidx = i
print("myidx = ", myidx)
