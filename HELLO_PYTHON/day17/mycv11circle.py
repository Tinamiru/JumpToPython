import cv2

img = cv2.imread('Lenna.png')

cv2.circle(img, (300, 300), 70, (0, 255, 255), -1)

cv2.imshow('img', img)

cv2.waitKey()
cv2.destroyAllWindows()
