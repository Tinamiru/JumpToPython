import cv2
import numpy as np

img = cv2.imread('startup.png')

rows, cols = img.shape[0:2]
d45 = 45.0 * np.pi / 180

m45 = np.float32([[ np.cos(d45), -1 * np.sin(d45), rows // 2],
                    [np.sin(d45), np.cos(d45), -1 * cols // 4]])

r45 = cv2.warpAffine(img, m45, (cols, rows))
cv2.imshow('img', img) 
cv2.imshow('45', r45) 

cv2.waitKey(0)
cv2.destroyAllWindows()
