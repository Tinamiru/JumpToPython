import cv2

img = cv2.imread('startup.png')

print(img)

print("img",type(img))

resize = cv2.resize(img, (500, 300))

cv2.imshow('img', resize)
cv2.imwrite("./startup.jpg", resize)

cv2.waitKey(0)
cv2.destroyAllWindows()