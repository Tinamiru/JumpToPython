import cv2

img1 = cv2.imread('b.png')
# 36  28 237 RED
# 76 177  34 Green
# 204 72  63 blue
print(img1)

cv2.imshow('img1', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()