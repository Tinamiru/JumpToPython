from keras.datasets import mnist
from keras import models
from keras import layers
import numpy as np
from tensorflow.python.keras.utils.np_utils import to_categorical

train_images_a = [
    [1, 0, 0, 0, 0,  0, 0, 0, 0],
    [0, 1, 0, 0, 0,  0, 0, 0, 0],
    [0, 0, 1, 0, 0,  0, 0, 0, 0],
    [0, 0, 0, 1, 0,  0, 0, 0, 0],
    [0, 0, 0, 0, 1,  0, 0, 0, 0],
    [0, 0, 0, 0, 0,  1, 0, 0, 0],
    [0, 0, 0, 0, 0,  0, 1, 0, 0],
    [0, 0, 0, 0, 0,  0, 0, 1, 0],
    [0, 0, 0, 0, 0,  0, 0, 0, 1]
]

train_labels_a = [
    0, 1, 2, 3, 4, 5, 6, 7, 8
]

train_images = np.array(train_images_a)
train_labels = np.array(train_labels_a)

train_labels_c = to_categorical(train_labels)

model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(9,)))
model.add(layers.Dense(9, activation='softmax'))

model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

model.fit(train_images, train_labels_c, epochs=5, batch_size=128)
loss, accuracy = model.evaluate(train_images, train_labels_c)

predict_result = model.predict(train_images)

model.save('mnist_hit.h5')

# for data in predict_result:
#     ai_anser = np.argmax(data)
#     print(ai_anser, end=",")
# print()
# print(train_labels)
