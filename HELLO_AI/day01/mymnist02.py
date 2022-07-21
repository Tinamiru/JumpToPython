# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import cv2

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# print("train_images", train_images.shape)
# print("train_labels", train_labels.shape)
#
# print("test_images", test_images.shape)
# print("test_labels", test_labels.shape)
#
img = test_images
img_label = test_labels
# for row in test_images[2]:
#     for data in row:
#         print(data, end="\t")
#     print("")
    
# print("img",type(img))
# cv2.imshow('img', img)
for idx, data in enumerate(img):
    print("train_labels["+str(idx)+"]= ", img_label[idx])
    cv2.imwrite("./test/" + str(idx) + ".png", img[idx])
