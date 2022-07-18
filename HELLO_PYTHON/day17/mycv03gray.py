import cv2

img1 = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE )

print(img1)

print("img1",type(img1))

cv2.imshow('img1', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()