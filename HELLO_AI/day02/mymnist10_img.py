# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import numpy as np
import cv2

train_images = []
for i in range(60000):
    print(i)
    load_img = cv2.imread("train/{}.png".format(i), cv2.IMREAD_GRAYSCALE)
    train_images.append(load_img)
    
train_images = np.array(train_images)

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

model = models.load_model("mnist.h5")

predict_result = model.predict(train_images)
ai_answer = np.argmax(predict_result[0])

print("ai_answer", ai_answer)