from keras.datasets import mnist
from keras import models
from keras import layers
import numpy as np
from tensorflow.python.keras.utils.np_utils import to_categorical

train_images_a = [
    [1, 0],
    [0, 1],
]

train_labels_a = [
    0, 1
]

train_images = np.array(train_images_a)
train_labels = np.array(train_labels_a)

train_labels_c = to_categorical(train_labels)

model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(2,)))
model.add(layers.Dense(2, activation='softmax'))

model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

model.fit(train_images, train_labels_c, epochs=5, batch_size=128)
loss, accuracy = model.evaluate(train_images, train_labels_c)

predict_result = model.predict(train_images)

model.save('mnist_holl.h5')
