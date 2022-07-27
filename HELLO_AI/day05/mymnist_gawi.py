# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
import numpy as np
from keras.utils.np_utils import to_categorical

train_images_a = [
    [0, 0],
    [0, 0.5],
    [0, 1],
    
    [0.5, 0],
    [0.5, 0.5],
    [0.5, 1],
    
    [1, 0],
    [1, 0.5],
    [1, 1]
]

train_labels_a = [
    0, 1, 2, 2, 0, 1, 1, 2, 0
]

train_images = np.array(train_images_a)
train_labels = np.array(train_labels_a)

train_labels_c = to_categorical(train_labels)
print("train_labels_c", train_labels_c)

model = models.Sequential()
model.add(layers.Dense(1024, activation='relu', input_shape=(2,)))
model.add(layers.Dense(1024, activation='relu'))
model.add(layers.Dense(3, activation='softmax'))

model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

model.fit(train_images, train_labels_c, epochs=30, batch_size=6)

predict_result = model.predict(train_images)
print("predict_result")
print(predict_result)

for data in predict_result:
    ai_anser = np.argmax(data)
    print(ai_anser, end=",")
print()
print(train_labels_a)

