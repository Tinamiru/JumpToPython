import cv2

img = cv2.imread('Lenna.png',cv2.IMREAD_GRAYSCALE)
print("img",type(img))
cv2.imshow('img', img)

cv2.imwrite("./Lenna_GrayScale.png", img)

cv2.waitKey(0)
cv2.destroyAllWindows()