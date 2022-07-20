import cv2

img = cv2.imread('r.png')
print("img",type(img))
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()