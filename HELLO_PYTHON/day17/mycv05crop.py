import cv2

img = cv2.imread('startup.png')
dst = img[50:1000, 300:850].copy()

cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
