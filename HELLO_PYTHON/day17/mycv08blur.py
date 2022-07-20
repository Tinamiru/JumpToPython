import cv2

img = cv2.imread('Lenna.png')
print("img",type(img))

blurimg = cv2.blur(img, (5000,5000))
cv2.imshow('img', blurimg)

cv2.waitKey(0)
cv2.destroyAllWindows()