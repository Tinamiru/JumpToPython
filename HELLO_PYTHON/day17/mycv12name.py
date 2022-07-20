import cv2

img1 = cv2.imread('startup.png')
cv2.putText(img1, "suzi", (450,200), 0, 2, (0, 0, 0), 2, 1, False)
print(img1)

cv2.imshow('img1', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()